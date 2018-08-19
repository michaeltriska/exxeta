.PHONY: docs clean

VIRTUALENV_DIR=${PWD}/env
PYTHON=${VIRTUALENV_DIR}/bin/python
PIP=${VIRTUALENV_DIR}/bin/pip


all:
	virtualenv -p python3 $(VIRTUALENV_DIR) --no-site-packages
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

start:
	$(PYTHON) service.py --max_grace_seconds=0 --logfile=-
