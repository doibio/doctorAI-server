import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY,
    title TEXT,
    content TEXT
)
''')

# Insert a single entry
cursor.execute('''
INSERT INTO conversations (title, content) VALUES (?, ?)
''', ('Sample Conversation', 'This is the content of the first conversation.'))

# Commit the transaction
conn.commit()

# Close the database connection
conn.close()

