# VorsichtAuto

## Managing dependencies and virtual environments - uv

To update packages and/or create a virtual environment run
```bash
uv sync
```

To add packages, run:
```bash
uv add <package>
```

To run a python command in the created virtual environment, either run:
```bash
uv run <command to run, e.g. python main.py>
```
or activate virtual environment
```bash
.venv/bin/activate
```

## Using dvc

Install:
```bash
uv tool install dvc
```