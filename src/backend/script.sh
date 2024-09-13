#!/bin/bash
python3.12 create_db.py
alembic upgrade head
python3.12 main.py
