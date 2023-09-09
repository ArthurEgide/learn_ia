PYTHON = python
project_picker_tmp_file = "_tmp"

choice_project:
	@python project_scanner.py

build: choice_project
	@echo "Welcome to my learning project"
	@read PROJECT_PATH < _tmp; \
	PROJECT_NAME=$(shell cat $(project_picker_tmp_file) | rev | cut -d'/' -f1 | rev); \
	docker build --build-arg PROJECT_NAME=$$PROJECT_NAME --build-arg PROJECT_PATH=$$PROJECT_PATH -t $$PROJECT_NAME .;
	rm _tmp

bash_container: choice_project
	@read PROJECT_PATH < _tmp; \
	PROJECT_NAME=$(shell cat $(project_picker_tmp_file) | rev | cut -d'/' -f1 | rev); \
	docker run -v ./$$PROJECT_PATH:/$$PROJECT_NAME --rm -it $$PROJECT_NAME bash
	rm _tmp

run_container: choice_project
	@read PROJECT_PATH < _tmp; \
	PROJECT_NAME=$(shell cat $(project_picker_tmp_file) | rev | cut -d'/' -f1 | rev); \
	docker run -v ./$$PROJECT_PATH:/$$PROJECT_NAME --rm -itd $$PROJECT_NAME
	rm _tmp

run_main_container: choice_project
	@read PROJECT_PATH < _tmp; \
	PROJECT_NAME=$(shell cat $(project_picker_tmp_file) | rev | cut -d'/' -f1 | rev); \
	docker run -v ./$$PROJECT_PATH:/$$PROJECT_NAME --rm $$PROJECT_NAME python main.py
	rm _tmp

