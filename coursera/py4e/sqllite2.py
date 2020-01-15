import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
conn.commit()

fh = open('C:\\Users\\volna\\Documents\\Coursera-Python\\test-data\\mbox.txt')

for line in fh:
    if not line.startswith('From: '): continue
    domain = re.findall("From: .*@(\S+)", line)[0]
    # print("domain:", domain)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
conn.commit()


for row in cur.execute("SELECT * FROM Counts ORDER BY count DESC LIMIT 3"):
    print(row[0], row[1])

conn.close()
