
install:
	pip install twine
	python -m pip install --upgrade build
	python -m pip install --upgrade virtualenv
	poetry install

build:
	python -m build

test-upload:
	twine upload -r testpypi dist/*

upload:
	twine upload dist/*
