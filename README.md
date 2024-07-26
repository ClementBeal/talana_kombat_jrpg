# Talana Komba JRPG

Fight simulation between 2 players. It uses JSON data to do the simulation.

The API is available under `http://0.0.0.0:8000`

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

`gunicorn --bind 0.0.0.0:8000 --reload -w 4 "talaka_kombat_jrpg:create_app()"`

## Test the API with cURL

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2":{"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}' \
     http://localhost:8000/simulate_fight
```

## How to build and run the Docker image

To build :

`docker build -t talana_kombat_jrpg .`

To run :

`docker run -d -p 8000:8000 talana_kombat_jrpg`