import sqlite3 as sql

def createDB():
  conn = sql.connect("data.db")
  conn.commit()
  conn.close()

def createTable():
  conn = sql.connect("data.db")
  cursor = conn.cursor()
  cursor.execute(
    """CREATE TABLE proyectos(
      
    )"""
  )

if __name__ == "__main__":
  createDB()