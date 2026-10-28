import os
from pathlib import Path

# Template for database and credential configuration
# Duplicate this file as db_config.py or use .env to set your actual credentials.

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "Admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "your-admin-password")

CSV_FILE = os.getenv("CSV_FILE", "feedback.csv")

# Database credentials
DB_TYPE = os.getenv("DB_TYPE", "csv")             # 'csv', 'sqlite', 'mysql', 'postgresql'
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your-db-password")
DB_NAME = os.getenv("DB_NAME", "sentiment_db")
