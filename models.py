from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Distro(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(80), nullable=False, unique=True)  # Distribution name (must be unique)
    version = db.Column(db.String(20), nullable=True)  # Optional version
    release_date = db.Column(db.Date, nullable=True)  # Release date of the distribution
    architecture = db.Column(db.String(20), nullable=False, default="x86_64")  # CPU architecture (default: x86_64)
    website = db.Column(db.String(200), nullable=True)  # Official website of the distribution

    def __repr__(self):
        return f"<Distro {self.name} {self.version}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'version': self.version,
            'release_date': self.release_date.isoformat() if self.release_date else None,
            'architecture': self.architecture,
            'website': self.website
        }