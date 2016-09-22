init:
	pip install -r requirements.txt

homeworks-skeleton:
	python homeworks_skeleton.py

test:
	py.test tests/

.PHONY: init homeworks-skeleton