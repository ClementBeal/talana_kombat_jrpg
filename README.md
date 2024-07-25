# Talana Komba JRPG

## Set up the project

On Linux

```
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```
## Run the tests

`pytest`

## My hypothesis

- The fight data are always in the good format. We can't receive a wrong JSON

## How to build and run the Docker image

To build :

`docker build -t talana_kombat_jrpg .`

To run :

`docker run -d -p 8000:8000 talana_kombat_jrpg`