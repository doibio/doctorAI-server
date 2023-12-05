import sqlite3

def create_database():
    # Connect to SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('chatbot.db')

    # Create cursor object to execute SQL commands
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

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()

    
