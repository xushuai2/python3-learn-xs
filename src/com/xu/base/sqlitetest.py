#coding=utf-8
import sqlite3
from _sqlite3 import Cursor
conn = sqlite3.connect('D:/xuPySqlite.db')
cursor = conn.cursor();
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))');
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')');
num = cursor.rowcount;
print(num);
cursor.close()
conn.commit()
conn.close()

