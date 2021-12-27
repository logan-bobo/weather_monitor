# Weather API service

The weather API is build using `Python` and `FastAPI`

# Reasoning for fast API
- Fast to run and has similar performance with NodeJS and Go
- Designed to be non-complex 
- Great support

# Running the API
 - install requirements defined in `./requirements.txt`
 - `$ uvicorn main:app` to run in live development use `--reload`

# Running the tests 
 - As our tests and source code are in different directories we need to set the following environment variable `export PYTHONPATH=.`
 - From the api directory run the following `pytest -vqrA tests/api_test.py`