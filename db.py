from typing import Any
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",      
    user="root",
    password="root",
    database="learn_agent"
)


cursor = conn.cursor()

def query(sql: str):
    """Execute a SQL SELECT query and return all results."""
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        return f"Error executing query: {e}"


def execute(sql: str, values: tuple[Any] = ()):
    """Execute a SQL command (INSERT, UPDATE, DELETE)."""
    try:
        cursor.execute(sql, values)
        conn.commit()
        return f"{cursor.rowcount} rows affected."
    except Exception as e:
        return f"Error executing statement: {e}"