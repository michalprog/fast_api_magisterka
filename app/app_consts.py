import os

# Stałe aplikacji
APP_NAME = "FastAPI Magisterka"
APP_VERSION = "1.0.0"

# PostgreSQL (z ENV albo fallback do wartości lokalnych)
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
DB_HOST = os.getenv("DB_HOST", "localhost")  # w docker-compose → "postgres"
DB_PORT = int(os.getenv("DB_PORT", 8090))    # w docker-compose → 5432
DB_NAME = os.getenv("DB_NAME", "postgres")

# Złożony URL do bazy (SQLAlchemy + psycopg2)
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# MongoDB config
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")  # w docker-compose → "mongo"
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "magisterka_database")

# Nazwy kolekcji
MONGO_COLLECTION_RECORD = "MongoRecord"
MONGO_COLLECTION_PERSON = "MongoPerson"
