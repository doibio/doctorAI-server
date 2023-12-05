import sqlite3

def create_database():
    # Connect to SQLite database
    conn = sqlite3.connect('chatbot.db')
    cur = conn.cursor()

    # Create 'users' table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY
        )
    ''')

    # Create 'conversations' table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            conversation_id TEXT PRIMARY KEY,
            user_id TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
    ''')

    # Create 'messages' table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            message_id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id TEXT,
            text TEXT,
            sender TEXT,
            FOREIGN KEY(conversation_id) REFERENCES conversations(conversation_id)
        )
    ''')

    # Insert test user
    cur.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', ('12345',))

    # Insert test conversation
    cur.execute('INSERT OR IGNORE INTO conversations (conversation_id, user_id) VALUES (?, ?)', ('67890', '12345'))

    # Insert test messages
    test_messages = [
        ('67890', 'Hello, how can I help you?', 'assistant'),
        ('67890', 'I have a question about my account.', 'user')
    ]
    cur.executemany('INSERT INTO messages (conversation_id, text, sender) VALUES (?, ?, ?)', test_messages)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()

    
