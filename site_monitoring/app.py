from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Site, Log
from tasks import check_site_status
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)  # Adicione esta linha

@app.route('/sites', methods=['POST'])
def add_site():
    data = request.get_json()
    new_site = Site(url=data['url'])
    db.session.add(new_site)
    db.session.commit()
    check_site_status.delay(new_site.id)
    return jsonify({'message': 'Site added and check initiated'}), 201

@app.route('/sites', methods=['GET'])
def list_sites():
    sites = Site.query.all()
    return jsonify([{'id': site.id, 'url': site.url} for site in sites])

@app.route('/sites/<int:site_id>/logs', methods=['GET'])
def get_logs(site_id):
    logs = Log.query.filter_by(site_id=site_id).all()
    return jsonify([{'status_code': log.status_code, 'response_time': log.response_time, 'timestamp': log.timestamp} for log in logs])

if __name__ == '__main__':
    app.run(debug=True)