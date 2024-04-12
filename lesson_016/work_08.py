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

cur.execute('delete from Orders where OrderID = "10"')
conn.commit()

cur.execute('insert into Orders (OrderID, CustomerID, EmployeeID) values ("10","Anton","5")')
# cur.execute('insert into Orders values ("10","2020-10-10","RJ","1000")')
conn.commit()

cur.execute('select * from Orders')
res = cur.fetchall()
print(res)

cur.execute('select * from Orders where OrderID = "10"')
res = cur.fetchall()
print(res)

conn.close()