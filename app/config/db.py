from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(50), nullable = False)
    is_active = db.Column(db.Bool, nullable = False)
# class Heladeria(db.Model):

#     id = db.Column(db.Integer, primary_key = True)

# class Producto(db.Model):
#     pass

# class Ingrediente(db.Model):
#     pass