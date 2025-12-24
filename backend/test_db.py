from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT name FROM sys.tables")
for row in cursor.fetchall():
    print(row.name)

conn.close()
