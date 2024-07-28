import sqlite3
import os
from dotenv import load_dotenv 
from flask import g

load_dotenv() 

DB_NAME = os.getenv("DATABASE_NAME")
 
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("videos.db")
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS videos ( title VARCHAR(500) NOT NULL , url VARCHAR(500) NOT NULL,comment VARCHAR(500))")
    cursor.execute(
        """
        INSERT INTO videos (title,url,comment)
        VALUES
        ('System Design Concepts Course and Interview Prep','https://www.youtube.com/watch?v=F2FmTdLtb_4','This course is around 1h'),
        ('Harvard CS50 (2023) – Full Computer Science University Course','https://www.youtube.com/watch?v=LfaMVlDaQ24','This course is around 1h'),
        ('ASP.NET Core Crash Course - C# App in One Hour','https://www.youtube.com/watch?v=BfEjDD8mWYg','This course is around 1h');
        
        """
        )
        
    conn.commit()
    cursor.close()

