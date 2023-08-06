from libsg.assets import AssetDb
from libsg.geo import Transform
from libsg.scene_types import BBox3D, Point3D, ObjectSpec, PlacementSpec, SceneState
from libsg.scene import ModelInstance, Scene
from libsg.simulator import Simulator
from libsg.simscene import SimScene

import random
import sys
from dataclasses import dataclass
from typing import Union

@dataclass
class Placement:
    position: Point3D = None
    up: Point3D = None
    front: Point3D = None
    object: ModelInstance = None
    ref_object: Union[ModelInstance,str] = None
    spec: PlacementSpec = None


class ObjectPlacer:
    def __init__(self, model_db: AssetDb):
        self.__model_db = model_db

    def _resolve_placement_spec(self, placement_spec: PlacementSpec, scene: Scene, object_to_place: ModelInstance) -> Placement:
        placement = Placement(object=object_to_place, spec=placement_spec)
        if placement.spec.type == 'placement_point':
            # "placement": {"position": [x, y, z]}
            placement.position = placement_spec.position
        elif placement_spec.type == 'placement_relation':
            # "placement": {"reference": ObjectSpec, "relation": "on|next"}
            placement.ref_object = self._resolve_object_spec_to_element_in_scene(scene, placement_spec.reference)
            if placement_spec.relation == 'next':
                placement = self._place_next(scene, placement)
            elif placement_spec.relation == 'on':
                placement = self._place_on(scene, placement)
        else:
            print(f'Unsupported placement_spec.type={placement_spec.type}', file=sys.stderr)
        return placement

    def _place_on(self, scene: Scene, placement: Placement) -> Placement:
        if placement.ref_object.type == 'ModelInstance':
            print(f'Place {placement.object.model_id} {placement.spec.relation} {placement.ref_object.model_id}', file=sys.stderr)
            sim = Simulator(mode='direct', verbose=False, use_y_up=False)
            sim_scene = SimScene(sim, scene, self.__model_db.config)
            placement.position = self._sample_position_on(sim_scene, placement.ref_object.id)
        else:
            bbox3D = placement.ref_object.bbox3D
            print(f'Place {placement.object.model_id} {placement.spec.relation} {placement.ref_object.type} with {bbox3D}', file=sys.stderr)
            obj_metadata = self.__model_db.get_metadata(placement.object.model_id)
            if placement.ref_object.type == 'Wall':
                placement.front = placement.ref_object.front.tolist()
                placement.up = placement.ref_object.up.tolist()
                m = [obj_metadata.dims[0], obj_metadata.dims[1]]
                placement.position = placement.ref_object.sample_face(margin=m).tolist()
            elif placement.ref_object.type == 'Floor':
                placement.position = bbox3D.get_face_center(BBox3D.TOP).tolist()
            elif placement.ref_object.type == 'Ceiling':
                placement.position = bbox3D.get_face_center(BBox3D.BOTTOM).tolist()
            else:
                print(f'Unsupported ref_object.type={placement.ref_object.type}', file=sys.stderr)
        return placement

    def _place_next(self, scene: Scene, placement: Placement) -> Placement:
        # get bbox of ref object
        sim = Simulator(mode='direct', verbose=False, use_y_up=False)
        sim_scene = SimScene(sim, scene, self.__model_db.config, include_ground=True)

        #ref_obj_metadata = self.__model_db.get_metadata(placement.ref_object.model_id)
        ref_obj_bbox = sim.get_aabb(placement.ref_object.id)
        obj_bbox = sim.get_aabb(placement.object.id)
        scene_bbox = sim.get_aabb_all()

        placement_found = False
        tries = 1
        max_tries = 10
        while not placement_found and tries < max_tries:
            # sample position on one of side faces or front face of bbox (TODO use semantic front)
            side = random.choice([BBox3D.LEFT, BBox3D.RIGHT, BBox3D.FRONT, BBox3D.BACK])
            print(f'sample side {side} {ref_obj_bbox}')
            sidepoint = ref_obj_bbox.sample_face(side, margin=[0, 0])

            # go out along face normal by [1, 2.5] * half-width
            obj_side_h = obj_bbox.get_face_dims(side)[2] * 0.5
            side_outnormal = ref_obj_bbox.get_face_outnormal(side)
            offset = side_outnormal.scale(random.uniform(1, 2.5) * obj_side_h)
            position = Point3D.add(sidepoint, offset)
            if not scene_bbox.contains(position):
                print('sampled sidepoint outside scene, retrying...')
                tries += 1
                continue

            # find parent supporting ref_object with raycast (TODO use support hierarchy instead)
            ref_bottom = ref_obj_bbox.sample_face(BBox3D.BOTTOM, margin=[0, 0]).tolist()
            ref_bottom[2] -= 0.0001
            below_ref_bottom = list(ref_bottom)
            below_ref_bottom[2] -= 0.2
            parent_intersection = sim.ray_test(ref_bottom, below_ref_bottom)
            print('ref_bottom intersection', ref_bottom, below_ref_bottom, parent_intersection)

            if parent_intersection.id == -1:  # no parent found, naive 0 height placement
                position.z = 0.0
                placement.position = position.tolist()
                print('placement without parent', placement)
            else:  # parent was found, drop down to parent
                placement.position = self._drop_place(sim_scene, position)
                print('placement with parent', placement)

            placement_found = True

        return placement

    # Note: will return either object or architectural element
    def _resolve_object_spec_to_element_in_scene(self, scene: Scene, object_spec: ObjectSpec):
        object = None
        if object_spec.type == 'object_id':
            object = scene.get_element_by_id(object_spec.object)
        elif object_spec.type == 'model_id':
            objects = scene.find_objects_by_model_ids([object_spec.object])
            object = next(iter(objects), None)
        elif object_spec.type == 'category':
            if ObjectSpec.is_arch(object_spec):
                element_type = object_spec.object.capitalize()
                elements = scene.arch.find_elements_by_type(element_type)
                object = next(iter(elements), None)
            else:
#            metadata = self.__model_db.get_metadata_for_ids(scene.get_all_model_ids())
                query = self.__model_db.get_query_for_ids('fpModel', scene.get_all_model_ids())
                query = query + f' AND {object_spec.object}'
                results = self.__model_db.search(query, fl='fullId', fq='+source:fpModel', rows=18000)
                model_ids = list([result['fullId'] for result in results])
                objects = scene.find_objects_by_model_ids(model_ids)
                object = next(iter(objects), None)
        else:
            print(f'Unsupported object_spec.type={object_spec.type}', file=sys.stderr)
        return object

    def _resolve_object_spec_to_model_id(self, scene: Scene, object_spec: ObjectSpec, placement_spec: PlacementSpec = None):
        model_id = None
        if object_spec.type == 'object_id':
            model_id = scene.get_object_by_id(object_spec.object).model_id
        elif object_spec.type == 'model_id':
            model_id = object_spec.object
        elif object_spec.type == 'category':
            query = object_spec.object
            fq = '+source:fpModel'
            if placement_spec:
                reference_object_spec = PlacementSpec.get_placement_reference_object(placement_spec)
                if reference_object_spec:
                    reference_object = self._resolve_object_spec_to_element_in_scene(scene, reference_object_spec)
                    element_type = reference_object.type.lower()
                    if element_type == 'wall':
                        fq = fq + ' +support:vertical'
                    elif element_type == 'ceiling':
                        fq = fq + ' +support:top'
                    else: 
                        fq = fq + ' -support:top -support:vertical'
            results = self.__model_db.search(query, fl='fullId', fq=fq, rows=18000)
            model_ids = list([result['fullId'] for result in results])
            if len(model_ids) == 0:
                print(f'Cannot find object matching query "{query}" with filter "{fq}"')
            model_id = random.choice(model_ids)
        else:
            print(f'Unsupported object_spec.type={object_spec.type}', file=sys.stderr)
        return model_id

    # find position that is statically supported by reference_object
    def _sample_position_on(self, simscene: SimScene, reference_object_id: str):
        ref_obj_bbox = simscene.sim.get_aabb(reference_object_id)
        ref_obj_height = ref_obj_bbox.dims[2]
        ref_obj_margin = [0.1 * ref_obj_bbox.dims[0], 0.1 * ref_obj_bbox.dims[1]]
        position = ref_obj_bbox.get_face_center(BBox3D.TOP).tolist()

        placement_found = False
        tries = 1
        max_tries = 10
        while not placement_found and tries < max_tries:
            sampled_point = ref_obj_bbox.sample_face(BBox3D.TOP, margin=ref_obj_margin)
            top_point = sampled_point.tolist()
            top_point[2] += 0.1
            bottom_point = sampled_point.tolist()
            bottom_point[2] -= ref_obj_height
            intersection = simscene.sim.ray_test(top_point, bottom_point)
            print(f'try drop place {tries}/{max_tries}: {sampled_point} {intersection}')
            if (intersection.id == reference_object_id):
                position = intersection.position
                placement_found = True
            tries += 1

        return position

    def _drop_place(self, simscene: SimScene, start_position: Point3D):
        top_point = start_position.tolist()
        bottom_point = start_position.tolist()
        bottom_point[2] -= 3.0  # TODO more intelligent than just "3m down"
        intersection = simscene.sim.ray_test(top_point, bottom_point)
        position = intersection.position if (intersection.id != -1) else start_position
        return position

    def try_add(self, scene_state: SceneState,
                object_spec: ObjectSpec,
                placement_spec: PlacementSpec) -> SceneState:
        scene = Scene.from_json(scene_state)

        model_id = self._resolve_object_spec_to_model_id(scene, object_spec, placement_spec)
        model_instance = ModelInstance(model_id=model_id)
        added_model_instance = scene.add(model_instance, clone=True)
        added = [added_model_instance]

        metadata = self.__model_db.get_metadata(model_id)
        # print(f'metadata {metadata}')
        placement = self._resolve_placement_spec(placement_spec, scene, added_model_instance)
        added_model_instance.transform.set_translation(placement.position)
        rotation = Transform.get_alignment_quaternion(metadata.up, metadata.front, placement.up or scene.up, placement.front or scene.front)
        added_model_instance.transform.set_rotation(rotation)

        if not placement_spec.get('allow_collisions'):
            print(f'check collisions')
            ignore_object_ids = []
            if placement.ref_object is not None:
                ignore_object_ids.append(placement.ref_object.id)
            contacts = self.check_object_contacts(scene, added_model_instance.id, ignore_object_ids)
            tries = 1
            max_tries = 10
            while len(contacts) > 0 and tries < max_tries:
                print(f'has collisions {len(contacts)}, try different placement {tries}/{max_tries}')
                placement = self._resolve_placement_spec(placement_spec, scene, added_model_instance)
                added_model_instance.transform.set_translation(placement.position)
                ignore_object_ids[0] = placement.ref_object.id
                contacts = self.check_object_contacts(scene, added_model_instance.id, ignore_object_ids)
                tries += 1
            if len(contacts):
                scene.collisions = [k for k in contacts.keys()]

        scene.modifications.extend([{ 'type': 'added', 'object': a.to_json() } for a in added])
        return scene

    def check_object_contacts(self, scene, object_id, ignore_object_ids=None):
        sim = Simulator(mode='direct', verbose=False, use_y_up=False)
        sim_scene = SimScene(sim, scene, self.__model_db.config)
        sim.step()
        contacts = sim.get_contacts(obj_id_a=object_id) #, include_collision_with_static=True)
        #contacts = sim.get_contacts(object_id, include_collision_with_static=True)
        #print(f'contacts: {contacts}')
        if ignore_object_ids is not None:
            contacts = {pair: contact for pair,contact in contacts.items() if pair[1] not in ignore_object_ids}
        #print(f'filtered contacts: {contacts} {ignore_object_ids}')
        return contacts
