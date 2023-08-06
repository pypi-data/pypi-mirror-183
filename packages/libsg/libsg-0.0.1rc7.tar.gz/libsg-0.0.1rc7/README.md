# scene-builder

## Local testing:
```bash
pip install --upgrade build
python -m build
pip install -e .
```

## Running Scene Builder Flask App

Fetch stk/scenestate data and place under your `FLASK_BASEDIR`.

```bash
FLASK_BASEDIR=~/path/to/data flask --app libsg.app --debug run
```

```bash
curl localhost:5000/scene/retrieve/
```

```bash
curl -X POST -H 'Content-Type:application/json' -d @object_add_category_position.json http://127.0.0.1:5000/object/add -o object_add_category_position_output.json
```

```bash
curl -X POST -H 'Content-Type:application/json' -d @object_remove_category.json http://127.0.0.1:5000/object/remove -o object_remove_category_output.json
```

## Packaging

Below packaging follows guidelines at https://packaging.python.org/en/latest/tutorials/packaging-projects/
Generate tokens on pypi and store in `.pypirc` file as below:
```ini
[testpypi]
  username = __token__
  password = pypi-XXX
[pypi]
  username = __token__
  password = pypi-XXX
```

*NOTE*: uploads with a specific version are only allowed once.
Thus, be careful about current `version` tag in `pyproject.toml` file.

Deploying test package:
```bash
pip install --upgrade build twine
python -m build
python -m twine upload --repository testpypi dist/*
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps libsg
```

Deploying package to real pypi index is same as above except for much simpler upload and install commands:
```bash
python -m twine upload dist/*
pip install libsg
```