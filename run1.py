from flask import Flask, jsonify, abort
import sqlite3

app = Flask(__name__)

DATABASE = 'chatbot.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    return conn

@app.route('/users/<string:user_id>/conversations/<string:conversation_id>/messages', methods=['GET'])
def get_conversation_messages(user_id, conversation_id):
    conn = get_db_connection()
    cur = conn.cursor()

    # Check if the user exists
    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    if not cur.fetchone():
        conn.close()
        abort(404, description="User not found")

    # Check if the conversation exists
    cur.execute('SELECT * FROM conversations WHERE user_id = ? AND conversation_id = ?', (user_id, conversation_id))
    if not cur.fetchone():
        conn.close()
        abort(404, description="Conversation not found")

    # Retrieve messages
    cur.execute('SELECT * FROM messages WHERE conversation_id = ?', (conversation_id,))
    messages = cur.fetchall()
    conn.close()

    # Convert rows to a list of dicts
    messages_list = [dict(message) for message in messages]

    return jsonify(messages_list)

if __name__ == '__main__':
    app.run(debug=True)

    
