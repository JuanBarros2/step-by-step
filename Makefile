unit-tests:
	pipenv run pytest

lint:
	echo "Running black .........."
	black .
	echo "Running flake8 .........."
	flake8

setup:
	pipenv install
	pipenv install -d
