from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_conversation(conversation_id):
    conn = get_db_connection()
    conversation = conn.execute('SELECT * FROM conversations WHERE id = ?', (conversation_id,)).fetchone()
    print("conversation")
    print(conversation)
    conn.close()
    return conversation

@app.route('/conversations/<int:conversation_id>', methods=['GET'])
def conversation(conversation_id):
    conversation = get_conversation(conversation_id)
    if conversation is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(dict(conversation))

if __name__ == '__main__':
    app.run(debug=True)

    
