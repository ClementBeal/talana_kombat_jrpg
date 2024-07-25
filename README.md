# Talana Komba JRPG

## Set up the project

On Linux

```
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
pip install -r requirements.txt
```

## Run the tests

`pytest`

## My hypothesis

- The fight data are always in the good format. We can't receive a wrong JSON

## How to run locally the API

`gunicorn --bind 0.0.0.0:8000 -w 4 "talaka_kombat_jrpg:create_app()"`

## Test the API with cURL

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"player1": {"movimientos": ["D", "DSD"], "golpes": ["K", "P"]}, "player2": {"movimientos": ["SA", "ASA"], "golpes": ["K", "P"]}}' \
     http://localhost:8000/simulate_fight
```

## How to build and run the Docker image

To build :

`docker build -t talana_kombat_jrpg .`

To run :

`docker run -d -p 8000:8000 talana_kombat_jrpg`