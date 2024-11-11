# Remove Background

## Use

- Celery Work Activation

```bash
celery -A tasks.celery worker --loglevel=info
```

- Inicialização do Flask

```bash
flask run
```

- Adding a new website

```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "http://example.com"}' http://127.0.0.1:5000/sites
```

- List of websites

```bash
curl http://127.0.0.1:5000/sites
```

- Check log

```bash
curl http://127.0.0.1:5000/sites/[id]/logs
```

## Preparing the environment

### Linux (Ubuntu/Debian)

- Create a virtual environment

```bash
python3 -m venv .venv
```

- Activate the virtual environment

```bash
source .venv/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

### Windows

- Create a virtual environment

```bash
python -m venv .venv
```

- Activate the virtual environment

```bash
.venv\Scripts\activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

## Preparing Docker

- Navigate to Docker

```bash
cd Docker
```

- Create the containers

```bash
docker-compose up -d
```

- Verification (optional)

```bash
docker ps
```
