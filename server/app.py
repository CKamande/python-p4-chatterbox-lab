from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message
from routes.messages import messages_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)
app.register_blueprint(messages_bp)

@app.route('/messages')
def messages():
    return ''

@app.route('/messages/<int:id>')
def messages_by_id(id):
    return ''

if __name__ == '__main__':
    app.run(port=5555)
