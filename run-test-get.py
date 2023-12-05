import unittest
import requests

class TestChatbotAPI(unittest.TestCase):
    BASE_URL = "http://localhost:5000/"  
    USER_ID = "12345"
    CONVERSATION_ID = "67890"

    def test_retrieve_conversation_messages(self):
        """ Test retrieving messages from a specific conversation """
        url = f"{self.BASE_URL}users/{self.USER_ID}/conversations/{self.CONVERSATION_ID}/messages"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        messages = response.json()
        self.assertIsInstance(messages, list)
        for message in messages:
            self.assertIn("message_id", message)
            self.assertIn("text", message)
            self.assertIn("sender", message)

if __name__ == '__main__':
    unittest.main()
