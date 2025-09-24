# Używamy lekkiego obrazu Python
FROM python:3.12-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj requirements i zainstaluj zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę projektu
COPY . .

# Otwórz port aplikacji
EXPOSE 8080

# Komenda startowa FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
