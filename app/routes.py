from flask import Blueprint, jsonify, request
from app.models import User, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Welcome to FriendBook API!"})

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"error": "Missing required fields"}), 400
        
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    
    try:
        db.session.commit()
        return jsonify({
            "message": "User created successfully",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Username or email already exists"}), 400 