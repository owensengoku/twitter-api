# Ref: https://blog.horejsek.com/makefile-with-python/
.PHONY: help prepare-dev-ubuntu test lint run doc

PACKAGE=twitter-api
VERSION=v0.1.0
IMAGE=registry.hub.docker.com/owensengoku/$(PACKAGE):$(VERSION)
VENV_NAME=venv
VENV_ACTIVATE=$(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python
GUNICORN=${VENV_NAME}/bin/gunicorn

.DEFAULT: help
help:
	@echo "make prepare-dev-ubuntu"
	@echo "       prepare development environment, use only once"
	@echo "make test"
	@echo "       run tests"
	@echo "make run"
	@echo "       run project"
	@echo "make run-gunicron"
	@echo "       run project with gunicron"

prepare-dev-ubuntu:
	sudo apt-get -y install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
	sudo apt install python3-venv
	python3.6 -m venv $(VENV_NAME)
	make venv
	make dep

venv:
	source $(VENV_NAME)/bin/activate

dep: venv
	${PYTHON} -m pip install -r requirements.txt

test: venv
	${PYTHON} -m pytest

run: venv
	${PYTHON} server.py

run-gunicron: venv
	${GUNICORN} --bind ${APPLICATION_HOST}:${APPLICATION_PORT} \
	            -e TWITTER_API_CONSUMER_KEY=${TWITTER_API_CONSUMER_KEY} \
	            -e TWITTER_API_CONSUMER_SECRET=${TWITTER_API_CONSUMER_SECRET} \
	            server
docker-build:
	docker build -t $(IMAGE) .

docker-push:
	docker push $(IMAGE)
