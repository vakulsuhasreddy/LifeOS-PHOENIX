import sqlite3


# Database file stored locally
DB_NAME = "lifeos.db"


def get_connection():
    """Create a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)


def create_tables():
    """Create the habit journal table."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            habit_name TEXT NOT NULL,
            completed INTEGER NOT NULL,
            notes TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_habit(entry):
    """Save a habit entry into the database."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO habits (date, habit_name, completed, notes)
        VALUES (?, ?, ?, ?)
    """, (
        entry["date"],
        entry["habit_name"],
        int(entry["completed"]),
        entry["notes"]
    ))

    connection.commit()
    connection.close()


def get_habits():
    """Retrieve all saved habit entries."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM habits ORDER BY date DESC")
    records = cursor.fetchall()

    connection.close()
    return records


def delete_habit(habit_id):
    """Delete a habit entry using its ID."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM habits WHERE id = ?", (habit_id,))

    connection.commit()
    connection.close()
