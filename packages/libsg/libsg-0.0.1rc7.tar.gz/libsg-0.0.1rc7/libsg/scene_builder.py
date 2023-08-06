from libsg.assets import AssetDb
from libsg.object_placement import ObjectPlacer
from libsg.scene_types import SceneState, ObjectSpec, SceneSpec, PlacementSpec
from libsg.scene import Scene
from libsg.io import SceneExporter

import json
import sys
from easydict import EasyDict
from typing import List, Tuple


class SceneBuilder:
    def __init__(self, cfg):
        self.__base_solr_url = cfg.get('solr_url')
        self.__arch_db = AssetDb(cfg.get('arch_db'))
        self.__scene_db = AssetDb(cfg.get('scene_db'))
        self.__model_db = AssetDb(cfg.get('model_db'), solr_url = f'{self.__base_solr_url}/models3d')
        self.scene_exporter = SceneExporter()
        self.object_placer = ObjectPlacer(model_db = self.__model_db)

    def generate(self, scene_spec: SceneSpec) -> SceneState:
        pass

    def modify(self, scene_state: SceneState, description: str) -> SceneState:
        pass

    def retrieve(self, scene_spec: SceneSpec) -> SceneState:
        if scene_spec.type == 'id':
            scenestate_path = self.__scene_db.get(scene_spec.input)
            scenestate = json.load(open(scenestate_path, 'r'))
            return scenestate

    def object_remove(self, scene_state: SceneState,
                      object_spec: ObjectSpec) -> SceneState:
        scene = Scene.from_json(scene_state)
        object_spec = object_spec if isinstance(object_spec, EasyDict) else EasyDict(object_spec)

        removed = []
        if object_spec.type == 'object_id':
            id_to_remove = object_spec.object
            removed_obj = scene.remove_object_by_id(id_to_remove)
            if removed_obj is not None:
                removed.append(removed_obj)
        elif object_spec.type == 'model_id':
            model_id_to_remove = object_spec.object
            removed = scene.remove_objects(lambda obj: obj.model_id == model_id_to_remove)
        elif object_spec.type == 'category':
            results = self.__model_db.search(object_spec.object, fl='fullId', fq='+source:fpModel', rows=18000)
            model_ids = set([result['fullId'] for result in results])
            removed = scene.remove_objects(lambda obj: obj.model_id in model_ids)
        else:
            print(f'Unsupported object_spec.type={object_spec.type}', file=sys.stderr)

        scene.modifications.extend([{'type': 'removed', 'object': r.to_json()} for r in removed])
        return scene.to_json()

    def object_add(self, scene_state: SceneState,
                         object_spec: ObjectSpec,
                         placement_spec: PlacementSpec) -> SceneState:

        object_spec = object_spec if isinstance(object_spec, EasyDict) else EasyDict(object_spec)
        placement_spec = placement_spec if isinstance(placement_spec, EasyDict) else EasyDict(placement_spec)
        updated_scene = self.object_placer.try_add(scene_state, object_spec, placement_spec)

        if object_spec.type == 'category' and not placement_spec.get('allow_collisions'):
            tries = 1
            max_tries = 10
            while len(updated_scene.collisions) > 0 and tries < max_tries:
                print(f'has collisions {len(updated_scene.collisions)}, try different object {tries}/{max_tries}')
                updated_scene =  self.object_placer.try_add(scene_state, object_spec, placement_spec)
                tries += 1
            print(f'placed after trying {tries} models to avoid collisions')
        else:  # no collision checking or specific object instance
            print(f'placed without collision checking')
        return updated_scene.to_json()

    def object_add_multiple(self, scene_state: SceneState,
                            specs: List[Tuple[ObjectSpec,PlacementSpec]]) -> SceneState:
        new_scene_state = scene_state
        for spec in specs:
            new_scene_state = self.object_add(new_scene_state, spec['object_spec'], spec['placement_spec'])
        return new_scene_state
