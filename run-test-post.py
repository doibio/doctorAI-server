import unittest
from flask_testing import TestCase
from your_flask_app import app, get_db_connection

class FlaskTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['DATABASE'] = 'chatbot.db'
        return app

    def setUp(self):
        self.conn = get_db_connection()
        self.cur = self.conn.cursor()

    def tearDown(self):
        self.cur.close()
        self.conn.close()

    def test_post_conversation_message(self):
        test_user_id = 'test_user'
        test_conversation_id = 'test_conversation'
        test_message_content = {'content': 'Hello, this is a test message!'}

        response = self.client.post(
            f'/users/{test_user_id}/conversations/{test_conversation_id}/messages',
            json=test_message_content
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['status'], 'success')

        self.cur.execute('SELECT * FROM messages WHERE conversation_id = ?', (test_conversation_id,))
        message = self.cur.fetchone()
        self.assertIsNotNone(message)
        self.assertEqual(message['content'], test_message_content['content'])

if __name__ == '__main__':
    unittest.main()
