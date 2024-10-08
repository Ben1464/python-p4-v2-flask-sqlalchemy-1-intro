from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy db object here
db = SQLAlchemy()

# Example model
class SomeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
