# Wargaming_test

### Инструкции для запуска тестов

```
В терминале перейти в директорию, содержащую файл теста
```

```
Для запуска тестов ввести следующие команды:
```

##### For Linux
```
pip install -r requirements.txt
```

```
python3 ./create_and_fill_db.py
```

```
pytest --alluredir=/tmp/my_allure_results
```

##### For Windows
```
pip install -r requirements.txt
```

```
py ./create_and_fill_db.py
```

```
pytest --alluredir=/tmp/my_allure_results
```



```
Для просмотра отчетов о прохождении тестов ввести:
```

```
allure serve /tmp/my_allure_results
```
