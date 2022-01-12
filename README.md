# Weather Monitor

A web app designed to take in your location and provide you the current temperature in your area.

## Functionality

- A front end that will get the current location from your browser, then feed back the temperature for that location.

- An API that will take in a longitude and latitude and provide back a temperature

## Application - API

## Application - Front End

## Infrastructure

### API CI

The CI for the API is a pipeline that will

- Lint out python code
- Run our test suite to test our functions
- Build our container from our API source code
- Push to Docker Hub

### Front End CI

### Local development of the API and front end

For local development the API and front end can be ran using `docker-compose`.
