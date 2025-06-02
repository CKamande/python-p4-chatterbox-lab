from flask import Blueprint, request, jsonify
from models import db, Message

messages_bp = Blueprint('messages', __name__)

# GET /messages
@messages_bp.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.created_at.asc()).all()
    return jsonify([message.to_dict() for message in messages]), 200

# POST /messages
@messages_bp.route('/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    body = data.get('body')
    username = data.get('username')

    if not body or not username:
        return {'error': 'Body and username are required'}, 400

    new_message = Message(body=body, username=username)
    db.session.add(new_message)
    db.session.commit()

    return new_message.to_dict(), 201

# PATCH /messages/<int:id>
@messages_bp.route('/messages/<int:id>', methods=['PATCH'])
def update_message(id):
    message = Message.query.get(id)
    if not message:
        return {'error': 'Message not found'}, 404

    data = request.get_json()
    if 'body' in data:
        message.body = data['body']
    db.session.commit()

    return message.to_dict(), 200

# DELETE /messages/<int:id>
@messages_bp.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.get(id)
    if not message:
        return {'error': 'Message not found'}, 404

    db.session.delete(message)
    db.session.commit()
    return {}, 204
