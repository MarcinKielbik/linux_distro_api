from datetime import datetime
from flask import Flask, jsonify, request
from flask_restful import Api
from models import db, Distro
from config import Config
from flask_migrate import Migrate
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


migrate = Migrate(app, db)



@app.route('/distros', methods=['GET', 'POST'])
def handle_distros():
    if request.method == 'GET':
        distros = Distro.query.all()
        return jsonify([distro.to_dict() for distro in distros])
    
    elif request.method == "POST":
        data = request.get_json()

        # Remove 'id' if it's in the data, as it should be auto-generated
        if 'id' in data:
            del data['id']

        # Convert the release_date string to a Python date object
        if 'release_date' in data and data['release_date']:
            data['release_date'] = datetime.strptime(data['release_date'], '%Y-%m-%d').date()

        # Check if the distro already exists based on the name
        existing_distro = Distro.query.filter_by(name=data['name']).first()
        if existing_distro:
            return jsonify({"message": f"Distro with name '{data['name']}' already exists"}), 400

        # Create a new Distro object
        new_distro = Distro(**data)

        # Add to the session and commit to the database
        db.session.add(new_distro)
        db.session.commit()

        # Return the newly added distro as a response
        return jsonify(new_distro.to_dict()), 201

    if request.method == 'GET':
        distros = Distro.query.all()
        return jsonify([distro.to_dict() for distro in distros])
    
    elif request.method == "POST":
        data = request.get_json()

        # Remove 'id' if it's in the data, as it should be auto-generated
        if 'id' in data:
            del data['id']

        # Convert the release_date string to a Python date object
        if 'release_date' in data and data['release_date']:
            data['release_date'] = datetime.strptime(data['release_date'], '%Y-%m-%d').date()

        # Create a new Distro object
        new_distro = Distro(**data)

        # Add to the session and commit to the database
        db.session.add(new_distro)
        db.session.commit()

        # Return the newly added distro as a response
        return jsonify(new_distro.to_dict()), 201


@app.route('/distros/<int:distro_id>', methods=['GET'])
def get_distro(distro_id):
    distro = Distro.query.get(distro_id)
    if distro:
        return jsonify(distro.to_dict())
    return jsonify({"message": "Distro not found"}), 404


from datetime import datetime

@app.route('/distros/<int:distro_id>', methods=['PUT'])
def update_distro(distro_id):
    distro = Distro.query.get(distro_id)
    if not distro:
        return jsonify({"message": "Distro not found"}), 404

    data = request.get_json()

    for key, value in data.items():
        if hasattr(distro, key):
            if key == "release_date" and isinstance(value, str):
                try:
                    value = datetime.strptime(value, "%Y-%m-%d").date()
                except ValueError:
                    return jsonify({"message": "Invalid date format. Use YYYY-MM-DD"}), 400

            setattr(distro, key, value)

    db.session.commit()
    return jsonify(distro.to_dict()), 200


    
@app.route('/distros/<int:distro_id>', methods=['DELETE'])
def delete_distro(distro_id):
    distro = Distro.query.get(distro_id)
    if distro:
        db.session.delete(distro)
        db.session.commit()
        return jsonify({"message": "Distro deleted"}), 200
    return jsonify({"message": "Distro not found"}), 404


@app.route('/')
def index():
    return 'Index Page'

if __name__ == '__main__':
    app.run(debug=True)