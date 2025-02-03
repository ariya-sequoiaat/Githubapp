
# GitHub Repository Info CLI

This is a Python CLI tool to fetch GitHub repository details such as branches, stars, and forks, and save the data into a CSV file. The tool fetches repository information using the GitHub API, validates input, and provides detailed logging for each step.

## Features

- Fetch GitHub repository details (branches, stars, forks).
- Validate input for correct GitHub username and repository name format.
- Write the details into a CSV file with a timestamp.
- Error handling with clear logging for missing files, invalid JSON, and API errors.

## Requirements

- Python 3.x
- `requests` library (for interacting with GitHub API)
- `pytest` (for testing)

## Installation








# GitHub Repository Info CLI

A Python CLI tool to fetch GitHub repository details and save them to CSV.

## Running with Docker

1. Build the Docker image:
   ```bash
   docker-compose build
   ```

2. Run the application:
   ```bash
   docker-compose run github-cli input.json
   ```

## Running Locally

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Run the application:
   ```bash
   poetry run python -m cli_app.main input.json
   ```

3. Run tests:
   ```bash
   poetry run pytest -svv tests
   ```

## Features

- Fetch GitHub repository details (branches, stars, forks)
- Validate input
- Write details to CSV with timestamp
- Comprehensive error handling and logging
```



Running program
cd cli_app$ python main.py input.json

Running pytest
cd FETGitHub$ pytest -svv tests

Docker Run
cd FETGitHub$ sudo apt update -y
cd FETGitHub$ sudo apt install docker.io -y
cd FETGitHub$ docker build -t aryaapp:latest .
FETGitHub$ docker run --rm aryaapp:latest

Docker compose Build
cd FETGitHub$ docker-compose build

Docker compose Run
cd FETGitHub$ docker-compose run --rm aryaapp sh 
python -m cli_app.main /app/cli_app/input.json
