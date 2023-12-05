from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/conversations/1', methods=['GET'])
def get_first_conversation():
    return jsonify({
        'id': 1,
        'title': 'First Conversation',
        'content': 'Hello, this is the first conversation!'
    })

if __name__ == '__main__':
    app.run(debug=True)


    
