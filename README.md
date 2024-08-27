# Vue/Nuxt 3 and Fast API Url Shortener

This is a simple URL shortener built with Vue/Nuxt 3 and Fast API. It uses SQLite as the database.

## Setup

The project can be run using Docker. To run the project, use the following command:
```bash
docker-compose up --watch
```

We use the `--watch` flag to rebuild the project when changes are made in specific directories.

PS: It works well for API, but frontend need to be setup for development environment. So, it is better to run the frontend manually using the following commands for now.

```bash
cd frontend
pnpm install
pnpm run dev
```

PS.2: Since API is build on a docker container, you're going to have errors on your IDE, you have two options:
1. Use the API container as a remote interpreter for your IDE.
2. Run the API manually using the following commands (But there's no point in using docker-compose if you're going to do this):
```bash
cd backend
pip install -r requirements.txt
#(Optional) Run the API if you're not using docker-compose
fastapi run run.py --reload
```

## Usage

### Migration

The project uses Alembic for database migrations.

To run the migrations and create the tables, run the following command:
```bash
docker-compose exec api alembic upgrade head
```

To create a new migration after adding/modifying models, run the following command:
```bash
docker-compose exec api alembic revision --autogenerate -m "migration message"
```

Note: The migrations are stored in the `api/migrations/versions` directory.

If you add a new model, you need to import it in the `api/app/core/models/__init__.py` file to make it available for Alembic.



