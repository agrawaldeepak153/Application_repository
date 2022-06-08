from multiprocessing import connection
import sqlite3

from colorama import Cursor
connection = sqlite3.connect('mydb.db')

cursor = connection.cursor()
create_tabel = "CREATE TABLE users (id int,username text,userpassword text)"
cursor.execute(create_tabel)

user = (1,'deepak','palak')
inser_qury = "INSERT INTO users values(?,?,?)"

cursor.execute(inser_qury,user)

user_list = [(2,'amit','palak1'),(3,'mannu','abcd')]
cursor.executemany(inser_qury,user_list)

select_qry = "SELECT * FROM users"
for i in cursor.execute(select_qry):
    print(i)

connection.commit()
connection.close()

