# Создание виртуального окружения

# python3.12 -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt

# 1 Создание бд postgresql

python3.12 create_db.py

# 2 Запуск последней миграции alembic

alembic upgrade head

# 3 Запуск сервера fastapi

python3.12 main.py
