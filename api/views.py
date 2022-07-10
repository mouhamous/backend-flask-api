from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from .models import db, User
from flask import json, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('settings.Config')
CORS(app)

db.init_app(app)
migrate = Migrate(app,db)


""" 
    function that authenticate user
    params: username, password
    return logged user info
"""
def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash( user.password,password):
        return user
    
"""
    return logged user data
"""
def identity(payload):
    user_id = payload['identity']

    return User.query.get(user_id)


jwt = JWT(app, authenticate, identity)

@app.route('/')
def test():
    return {'message': "ok"}

"""
    method: GET
    return logged in user information
"""
@app.route("/userinfo", methods=['GET'])
@jwt_required()
def logged_user_info():

    return current_identity.data()
    

"""
    this function allow user to update email account
    params: id 
    method: PUT
    return updated data
"""
@app.route("/users/<int:id>",methods=['PUT'])
@jwt_required()
def update_user(id):
    if id == current_identity.id:
        email = request.json.get('email')
        current_identity.email= email
        db.session.commit()
    return current_identity.data()

