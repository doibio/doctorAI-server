from flask import Flask, jsonify, abort

app = Flask(__name__)

conversations = {
    "12345": {
        "67890": [
            {"messageId": "1", "text": "Hello, how can I help you?", "sender": "assistant"},
            {"messageId": "2", "text": "I have a question about my account.", "sender": "user"}
        ]
    }
}

@app.route('/users/<string:user_id>/conversations/<string:conversation_id>/messages', methods=['GET'])
def get_conversation_messages(user_id, conversation_id):
    user_conversations = conversations.get(user_id)
    if not user_conversations:
        abort(404, description="User not found")

    messages = user_conversations.get(conversation_id)
    if messages is None:
        abort(404, description="Conversation not found")

    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)


    
