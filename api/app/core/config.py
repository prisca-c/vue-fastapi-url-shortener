import json
import os


class Config:
    CORS_ORIGINS = json.loads(os.getenv("API_CORS_ORIGINS", '["http://localhost", "http://localhost:3000"]'))
    DATABASE_URL = os.getenv("DATABASE_URL")
    HEADERS = json.loads(os.getenv("HEADERS", '["Content-Type", "Authorization"]'))
