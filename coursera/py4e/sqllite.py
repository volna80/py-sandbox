import sqlite3

conn = sqlite3.connect('C:\\Users\\volna\\Documents\\Coursera-Python\\sqllite\\one.db')

cur = conn.cursor()

cur.execute('DELETE FROM Ages')
cur.execute("INSERT INTO Ages (name, age) VALUES ('Keavan', 35)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Connolly', 14)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Aydon', 34)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Melania', 16)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Cassy', 23)")

conn.commit()

for row in cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X"):
    print(str(row[0]))

conn.close()