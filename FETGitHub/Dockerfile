# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the wheel file into the container (fix: add the destination path)
COPY cli-app/dist/cli_app-0.1.0-py3-none-any.whl /app/


# Install dependencies from the wheel file
RUN pip install cli_app-0.1.0-py3-none-any.whl

# Copy the content of the app into the container
#COPY cli-app/cli_app/main.py /app/

#COPY cli-app/cli_app/input.json /app/

# Set the command to run your Python CLI app (adjust for your main script)
#ENTRYPOINT ["python", "-m", "cli_app.main", "/app/cli_app/input.json"]
#ENTRYPOINT ["python", "-m", "cli_app.main", "input.json"]
