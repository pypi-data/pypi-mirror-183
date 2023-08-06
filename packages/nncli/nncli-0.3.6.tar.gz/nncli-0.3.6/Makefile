.POSIX:

.PHONY: clean clean-test clean-pycache clean-build help lint coverage coverage-html release dist install run debug docs

dist:
	flit build

clean: clean-build clean-pycache clean-test
	make -C docs clean

clean-build:
	rm -fr dist/

clean-pycache:
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -fr .tox

lint:
	pylint nncli tests --disable=parse-error
	vulture nncli .vulture_whitelist.py

test:
	python -m pytest

test-all:
	tox

coverage:
	python -m pytest --cov=nncli

coverage-html: coverage
	coverage html

release: dist
	twine upload -s dist/*

docs:
	make -C docs html man

install:
	flit install --deps=none

run:
	python -m nncli $(cmd)

debug: install
	pudb3 $$(which nncli) $(cmd)
