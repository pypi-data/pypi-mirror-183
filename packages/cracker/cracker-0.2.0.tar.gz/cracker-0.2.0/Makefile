build:
	python -m build

clean:
	find cracker -name "*.pyc" -exec rm {} +
	find cracker -name "__pycache__" -prune -exec rm -r {} +
	find cracker -name "*.egg-info" -prune -exec rm -r {} +
	rm -r build dist  2> /dev/null || true

upgrade:
	pip install --upgrade pip setuptools

install:
	pip install -e .

install-all:
	pip install -e .[dev,build]
