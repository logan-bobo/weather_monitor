# Weather API service

The weather API is build using `Python` and `FastAPI`

## Reasoning for fast API

- Fast to run and has similar performance to NodeJS and Go
- Designed to be non-complex and easy to pick up
- Great support

## Setting up venv

- Create venv `python3 -m venv weather-app`
- Enter venv `source weather-app/bin/activate`
- Install requirements defined in `./requirements.txt` with `pip3 install -r ./requirements.txt`
## Running the API

- To run the API execute `uvicorn main:app`

## Running the tests

- From the api directory run the following `python3 -m unittest tests/api_test.py`

## Access the pre-built API docs

- When the API is running, FastAPI will also generate its own documentation
 to access these running the server locally `http://127.0.0.1:8000/docs`.
