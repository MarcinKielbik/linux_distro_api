from flask import Flask, jsonify
from flask_restful import Api
from models import db, Distro
from config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


migrate = Migrate(app, db)


@app.route('/distros', methods=['GET'])
def get_all_distros():
    distros = Distro.query.all()
    return jsonify([distro.to_dict() for distro in distros])


@app.route('/distro/<int:distro_id>', methods=['GET'])
def get_distro(distro_id):
    distro = Distro.query.get(distro_id)
    if distro:
        return jsonify(distro.to_dict())
    return jsonify({"message": "User not found"}), 404


@app.route('/')
def index():
    return 'Index Page'

if __name__ == '__main__':
    app.run(debug=True)