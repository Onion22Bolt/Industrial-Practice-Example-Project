## Use an official Python runtime as a parent image
#FROM python:3.10
#
## Set the working directory to /app
#WORKDIR /app
#
## Copy the current directory contents into the container at /app
#COPY . /app
#
## Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt
#
## Run main.py when the container launches
#CMD ["uvicorn", "main:fastapi", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.10 AS build

# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Switch working directory
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy every content from the local file to the image
COPY . /app

# Second stage: Runtime
FROM python:3.10-slim

# Switch working directory
WORKDIR /app

# Copy the requirements file from the build stage
COPY --from=build /app/requirements.txt /app/requirements.txt

# Install the packages specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary files from the build stage
COPY --from=build /app /app

# Run the application
CMD ["uvicorn", "main:fastapi", "--host", "0.0.0.0", "--port", "8000"]

