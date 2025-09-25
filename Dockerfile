# Use an official Python runtime as a parent image
FROM python:3.14.0rc3-alpine3.21

ENV PYTHONUNBUFFERED=1

LABEL org.opencontainers.image.description="Automatically sync your All4Schools schedule with any CalDAV calendar application using Docker"
LABEL org.opencontainers.image.authors="Niklas Fuchs"
LABEL org.opencontainers.image.source = "https://github.com/xXxNIKIxXx/TimeSync"
LABEL org.opencontainers.image.licenses="MIT"

# Set the working directory in the container
WORKDIR /app

COPY . .

# Install g++ as well as other dependencies required by Python libraries and any needed packages specified in requirements.txt
RUN apk add --no-cache g++
RUN apk add --no-cache libxml2-dev
RUN apk add --no-cache libxslt-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["python", "./main.py"]