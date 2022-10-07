build:
	python -m build

test-upload:
	twine upload -r testpypi dist/*

upload:
	twine upload dist/*
