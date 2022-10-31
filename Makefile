install: # установка зависимостей
	poetry install
lint: # проверка кода линтеров python
	poetry run flake8 gendiff
build: # сборка проекта
	poetry build
package-install: # установка пакета
	python3 -m pip install --user dist/*.whl
test: # запуск тестов pytest
	poetry run pytest
test-coverage:
	poetry run pytest --cov-report term-missing --cov=gendiff_pack --cov-report xml
