# Use an official Python runtime
FROM python:alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#Flask Environment Variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=development

# Make port 5000 available to the world outside this container
EXPOSE 5000
# CD into the flask directory
WORKDIR /app/src/Flask

# Run main.py when the container launches
CMD ["flask","run"]

