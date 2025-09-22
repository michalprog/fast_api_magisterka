# Stałe aplikacji
APP_NAME = "FastAPI Magisterka"
APP_VERSION = "1.0.0"

# PostgreSQL
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = 8090
DB_NAME = "postgres"

# Złożony URL do bazy (SQLAlchemy + psycopg2)
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
# MongoDB config
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB_NAME = "magisterka_database"

# Nazwy kolekcji
MONGO_COLLECTION_RECORD = "MongoRecord"
MONGO_COLLECTION_PERSON = "MongoPerson"
