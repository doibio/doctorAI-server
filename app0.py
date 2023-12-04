from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conversations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(200))

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/conversations/<int:conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    conversation = Conversation.query.get(conversation_id)
    if conversation:
        return jsonify({
            'id': conversation.id,
            'title': conversation.title,
            'content': conversation.content
        })
    else:
        return jsonify({'error': 'Conversation not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
