# VorsichtAuto

## Downloading data

Data in the `/data` directory is tracked by dvc. To download data from COCO there is a script that downloads relevant images for traffic. To download, run

```bash
uv run download-coco
```

## Tools

### Managing dependencies and virtual environments - uv

To update packages and/or create a virtual environment run
```bash
uv sync
```

To add packages, run
```bash
uv add <package>
```

To run a python command in the created virtual environment, either run
```bash
uv run <command to run, e.g. python main.py>
```
or activate virtual environment
```bash
.venv/bin/activate
```

### Using dvc

Install dvc system-wide with
```bash
uv tool install dvc
```

To add artifacts or track changes run
```bash
dvc add data/<path to data/model>
```
This will create a `.dvc` file and write the actual data to `.gitignore` in `/data`.

We then track the dvc changes in git:
```bash
git add data/<path to data/model>.dvc data/.gitignore
```