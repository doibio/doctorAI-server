import unittest
import requests

class TestChatbotAPI(unittest.TestCase):
    BASE_URL = "http://localhost:5000/"
    USER_ID = "12345"
    CONVERSATION_ID = "67890"

    def test_post_conversation_message(self):
        """ Test posting a message to a specific conversation """
        url = f"{self.BASE_URL}users/{self.USER_ID}/conversations/{self.CONVERSATION_ID}/messages"
        
        data = {
            'message': 'Sample message text1',
        }
        
        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 201)

        response_data = response.json()
        print(response_data)
        self.assertIn('message', response_data)
        self.assertEqual(response_data['message'], 'Message sent successfully')
        self.assertIn('status', response_data)
        self.assertEqual(response_data['status'], 'success')

if __name__ == '__main__':
    unittest.main()


# import unittest
# import requests

# class TestChatbotAPI(unittest.TestCase):
#     BASE_URL = "http://localhost:5000/"  
#     USER_ID = "12345"
#     CONVERSATION_ID = "67890"

#     def test_retrieve_conversation_messages(self):
#         """ Test retrieving messages from a specific conversation """
#         url = f"{self.BASE_URL}users/{self.USER_ID}/conversations/{self.CONVERSATION_ID}/messages"
#         response = requests.get(url)

#         self.assertEqual(response.status_code, 200)

#         messages = response.json()
#         self.assertIsInstance(messages, list)
#         for message in messages:
#             self.assertIn("messageId", message)
#             self.assertIn("text", message)
#             self.assertIn("sender", message)

# if __name__ == '__main__':
#     unittest.main()


    # import unittest
# from flask_testing import TestCase
# from app import app, get_db_connection

# class FlaskTestCase(TestCase):

#     def create_app(self):
#         app.config['TESTING'] = True
#         app.config['DATABASE'] = 'chatbot.db'
#         return app

#     def setUp(self):
#         self.conn = get_db_connection()
#         self.cur = self.conn.cursor()

#     def tearDown(self):
#         self.cur.close()
#         self.conn.close()

#     def test_post_conversation_message(self):
#         test_user_id = '12345'
#         test_conversation_id = '67890'
#         test_message_text = {'text': 'Hello, this is a test message!'}

#         response = self.client.post(
#             f'/users/{test_user_id}/conversations/{test_conversation_id}/messages',
#             json=test_message_text
#         )

#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.json['status'], 'success')

#         self.cur.execute('SELECT * FROM messages WHERE conversation_id = ?', (test_conversation_id,))
#         message = self.cur.fetchone()
#         self.assertIsNotNone(message)
#         self.assertEqual(message['text'], test_message_text['text'])

# if __name__ == '__main__':
#     unittest.main()
