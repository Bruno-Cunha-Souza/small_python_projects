from celery import Celery
import requests
from models import db, Site, Log
from config import Config
from flask import Flask

# Crie a aplicação Flask
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

celery = Celery(__name__)
celery.conf.broker_url = 'redis://localhost:6379/0'
celery.conf.result_backend = 'redis://localhost:6379/0'

@celery.task
def check_site_status(site_id):
    with app.app_context():
        site = Site.query.get(site_id)
        if site:
            try:
                response = requests.get(site.url)
                log = Log(site_id=site.id, status_code=response.status_code, response_time=response.elapsed.total_seconds())
            except requests.RequestException as e:
                log = Log(site_id=site.id, status_code=0, response_time=0)
            db.session.add(log)
            db.session.commit()