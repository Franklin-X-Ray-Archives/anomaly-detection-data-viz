# anomaly-detection-data-viz

Dash app for anomaly data viz

### Installation

poetry install

### Execution

poetry run poe dev poetry run pre-commit install

docker build -t anom-data-viz .

docker run -p 8000:8000 –rm -ti -v $PWD:/app/project anom-data-viz bash
