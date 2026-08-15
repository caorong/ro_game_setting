.PHONY: install sync build validate test all clean

install:
	python -m pip install -e '.[dev]'

sync:
	python scripts/sync_rathena.py

build:
	python scripts/build_reference.py

validate:
	python scripts/validate_reference.py

test:
	pytest

all: validate test

clean:
	rm -rf generated vendor/rathena .pytest_cache
