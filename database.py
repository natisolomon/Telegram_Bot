import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create the students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        department TEXT,
        year TEXT,
        name TEXT,
        phone_number TEXT
    )
''')

# Sample data insertion (you can add as many records as needed)
students = [
    ("Computer Science", "4", "Tsion", "251-929-498-016"),
    ("Computer Science", "4", "Kena", "251-954-836-859"),
    ("Computer Science", "4", "Leta Eshetu", "251-945-266-234"),
    ("Computer Science", "4", "Samson Tariku", "251-900-762-478"),
    ("Computer Science", "4", "Abenezar", "0921124252"), 
    ("Computer Science", "2", "Bob", "234-567-8901"),
    ("IT", "1", "Charlie", "345-678-9012"),
    ("Accounting Degree", "4", "Kuku", "0929122966"),
    ("Accounting Degree", "3", "Lidia", "0913184253"),
    ("Accounting Degree", "4", "Bethel", "0940519822"),
    ("IT", "2", "Eve", "567-890-1234"),
    ("Accounting TVET", "3", "Diana", "456-789-0123"),
]

# Insert sample data into the database
cursor.executemany('INSERT INTO students (department, year, name, phone_number) VALUES (?, ?, ?, ?)', students)
conn.commit()

# Close the connection to the database
conn.close()
