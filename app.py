from flask import Flask, jsonify, abort, request
import sqlite3

app = Flask(__name__)

DATABASE = 'chatbot.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/users/<string:user_id>/conversations/<string:conversation_id>/messages', methods=['GET'])
def get_conversation_messages(user_id, conversation_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    if not cur.fetchone():
        conn.close()
        abort(404, description="User not found")

    cur.execute('SELECT * FROM conversations WHERE user_id = ? AND conversation_id = ?', (user_id, conversation_id))
    if not cur.fetchone():
        conn.close()
        abort(404, description="Conversation not found")

    cur.execute('SELECT * FROM messages WHERE conversation_id = ?', (conversation_id,))
    messages = cur.fetchall()
    conn.close()

    messages_list = [dict(message) for message in messages]

    return jsonify(messages_list)

@app.route('/users/<string:user_id>/conversations/<string:conversation_id>/messages', methods=['POST'])
def post_conversation_message(user_id, conversation_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    if not cur.fetchone():
        conn.close()
        abort(404, description="User not found")

    cur.execute('SELECT * FROM conversations WHERE user_id = ? AND conversation_id = ?', (user_id, conversation_id))
    if not cur.fetchone():
        conn.close()
        abort(404, description="Conversation not found")

    print(request.json.get('message'))
    message_text = request.json.get('message')
    if not message_text:
        conn.close()
        abort(400, description="No message text provided")

    cur.execute('INSERT INTO messages (conversation_id, text) VALUES (?, ?)', (conversation_id, message_text))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Message sent successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)

    
