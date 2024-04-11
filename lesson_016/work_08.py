import  sqlite3

conn = sqlite3.connect("data/base.sqlite")
# conn.text_factory = bytes
cur = conn.cursor()
cur.execute("select * from Orders where (Freight > 100) and (ShipRegion = 'RJ')")
results = cur.fetchall()
print(results)

cur.execute('select ContactName from Customers where ContactName like "%C%"')
res = cur.fetchall()
print(res)
