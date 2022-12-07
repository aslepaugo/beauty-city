# beuaty-city

## Как установить
Для написания скрипта использовался __Python 3.11.0__, подойдет 3.7 и выше

1. Склонировать репозиторий.
2. Создать виртуальное окружение.
```bash
python -m venv env
```
   
3. Установить зависимости:
```bash
pip install -r requirements.txt
```
1. Переименовать файл .env_copy в .env

```bash
mv .env_example .env
```

5. Отредактировать файл .env, 
Пример .env:
```
TG_BOT_TOKEN=958423683:AAEAtJ5Lde5YYfkjergber
```
*Как получить TELEGRAM_TOKEN: https://way23.ru/регистрация-бота-в-telegram.html

6. Активировать виртуальное окружение:

```bash
. env/bin/activate
```

## Запуск
```bash
python main.py
```
