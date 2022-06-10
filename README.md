# anomaly-detection-data-viz

Dash app for anomaly data viz

### Installation

poetry install

### Execution

poetry run poe dev poetry run pre-commit install

docker build -t anom-data-viz .

docker run -e .env -p 5000:5000 -v $PWD:/app/project anom-data-viz bash
