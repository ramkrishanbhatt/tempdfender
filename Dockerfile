FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure the directory for video storage exists
RUN mkdir -p /app/app/storage/videos

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
