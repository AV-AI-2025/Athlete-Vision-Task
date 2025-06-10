# Placeholder for SQLite setup
import sqlite3

def init_db():
    conn = sqlite3.connect("output/videos.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS videos
                 (id INTEGER PRIMARY KEY, filename TEXT, metrics TEXT)""")
    conn.commit()
    conn.close()
