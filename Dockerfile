# Use an official Python runtime
FROM python:3.12.3-slim

WORKDIR /app
COPY . /app
EXPOSE 5000

#Flask Environment Variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=development

# Install packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN rm requirements.txt

# CD into Flask directory
WORKDIR /app/src/Flask

# Run Flask when the container launches
CMD ["flask","run"]

