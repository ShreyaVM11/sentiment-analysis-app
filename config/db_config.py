import os
from pathlib import Path

# Load environment variables from .env file if python-dotenv is installed
try:
    from dotenv import load_dotenv
    # Look for .env in project root or in config folder
    base_dir = Path(__file__).resolve().parent.parent
    env_path = base_dir / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
    else:
        config_env = Path(__file__).resolve().parent / ".env"
        if config_env.exists():
            load_dotenv(dotenv_path=config_env)
except ImportError:
    pass

# ==========================================
# 🔐 Application & Admin Credentials
# ==========================================
# Flask session secret key
SECRET_KEY = os.getenv("SECRET_KEY", "1111")

# Admin dashboard login credentials
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "Admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "1110")

# ==========================================
# 🗄️ Database & Storage Configuration
# ==========================================
# Default CSV data storage (used by current app)
CSV_FILE = os.getenv("CSV_FILE", "feedback.csv")

# Database connection credentials (for MySQL / PostgreSQL / SQLite if configured)
DB_TYPE = os.getenv("DB_TYPE", "csv")             # 'csv', 'sqlite', 'mysql', 'postgresql'
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")        # Set your database password here or via .env
DB_NAME = os.getenv("DB_NAME", "sentiment_db")

# Helper function to get database URI if using SQLAlchemy or relational DBs
def get_database_uri() -> str:
    if DB_TYPE == "mysql":
        return f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    elif DB_TYPE == "postgresql":
        return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    elif DB_TYPE == "sqlite":
        return f"sqlite:///{DB_NAME}.db"
    return CSV_FILE
