# Use an official Python runtime
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# CD into the flask directory
WORKDIR /app/src/Flask

# Run main.py when the container launches
CMD [ "python","main.py" ]

