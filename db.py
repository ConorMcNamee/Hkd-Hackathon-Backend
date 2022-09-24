import sqlite3
import click
from flask import Flask, g, current_app


def init_db():
    connection = sqlite3.connect('database.db')
    print("Connetion opened")

    with open('schema.sql') as f:
        pass

    # Populating the database with data
    
    connection.commit()
    connection.close()

    print("DB Initialised!")

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

