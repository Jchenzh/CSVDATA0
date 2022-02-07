import sqlite3
dbfile = "test.db"
conn = sqlite3.connect(dbfile)

sql_str = f"insert into test01(Loop2, Step, Loop1) values({1},{2},{3});"
sql_str = "create table test01(apple, banana)"
conn.execute(sql_str)

class Table:
    def __init__(self, *args):
        pass
    def createtable(self):
    dbfile = "test.db"
    conn = sqlite3.connect(dbfile)
    sql_str =\
    f"""
    CREATE TABLE
    customers(
        C_Id
    INT,
    Name
    varchar(50),
    Address
    varchar(255),
    Phone
    varchar(20)
    );"""
    conn.execute(sql_str)


createtable()