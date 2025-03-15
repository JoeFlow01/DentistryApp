import sqlite3

class Database:
    def __init__(self):
        self.db_name = "my_database.db"
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                                    start_date TEXT,
                                    duration INTEGER,
                                    doc TEXT,
                                    room INTEGER,
                                    patient TEXT
                                )''')
        self.conn.commit()

    def get_appointments(self, date):
        """Retrieve appointments for a specific date safely"""
        self.cursor.execute('SELECT * FROM appointments WHERE start_date = ?', (date,))
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection"""
        self.conn.close()


# Example usage
db = Database()

# Retrieve appointments safely
appointments = db.get_appointments("15/03/2025")
print(appointments)  # Output: List of appointments

db.close()  # Close connection when done
