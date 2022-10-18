install: # установка зависимостей
	poetry install
lint: # проверка кода линтеров python
	poetry run flake8 gendiff
build: # сборка проекта
	poetry build
package-install: # установка пакета
	python3 -m pip install --user dist/*.whl
