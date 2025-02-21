# This dockerfile builds a docker image for the example site for development purposes only.
# WARNING: THIS IS NOT FOR USE IN PRODUCTION IN ANY SHAPE OR FORM.

# Use an official Python runtime as a parent image
FROM python:3.9
LABEL maintainer="hello@wagtail.io"

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# we're only going to copy the requirements for pip first, so if we're working
# on the example site and testing docker builds we don't have to rebuid the
# "pip requirements layers" every time we change a file.

# copy local pip dependences
COPY ./grapple /code/grapple
COPY ./setup.cfg /code/setup.cfg
COPY ./setup.py ./code/setup.py

# copy example site requires file
COPY ./tests/requirements.txt /code/tests/requirements.txt

WORKDIR /code/tests

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r ./requirements.txt
RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
COPY ./tests /code/tests
# Set the working directory to /code/

RUN python manage.py migrate

RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000
CMD exec gunicorn example.wsgi:application --bind 0.0.0.0:8000 --workers 3
