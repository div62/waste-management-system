import sqlite3
from pathlib import Path
DATABASE_FILE = Path(__file__).resolve().parent.parent / "bingo.db"
def get_connection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection