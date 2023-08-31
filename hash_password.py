from passlib.hash import sha512_crypt as sha
password = sha.hash('admin')
print(password)
from database import db

mydb = db('root', 'localhost', 'djnisarga#sj1415', 'bankingpayments')
query = "update users set password = '{}' where username = 'nisargadj'".format(password)

mydb.cursor.execute(query)
mydb.db.commit()