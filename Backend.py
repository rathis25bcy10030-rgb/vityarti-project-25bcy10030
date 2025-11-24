# ==========================================
# MODULE 1: DATABASE MANAGER (Backend Logic)
# ==========================================
import sqlite3 as sp

database="tracker.db"

def initialize():
    con=sp.connect(database)
    cur=con.cursor()
    #expenses
    cur.execute("create table if not exists expenses (id int primary key ,category text not null,amount real not null,date text not null, description text) ")
    #budget
    cur.execute("create table if not exists budget(id int primary key,total_limit raeel not null)")
    #defalut budget
    cur.execute("select count(*) from budget")
    a=cur.fetchone()
    if a[0]==0:
        cur.execute("insert into budget(id,total_limit) values (1,0.0)")
    con.commit()
    con.close()

def add_expense(category,amount,date,description):
    con=sp.connect(database)
    cur=con.cursor()
    cur.execute("insert into expenses(category,amount,date,description) values ({},{},{},{})",(category,amount,date,description))
    con.commit()
    con.close()

def fetch_expenses():
    con=sp.connect(database)
    cur=con.cursor()
    cur.execute("select * from expenses order by date desc")
    row=cur.fetchall()
    con.close()
    return row

def update(new_limit):
    con=sp.connect(database)
    cur=con.cursor()
    cur.execute("update budget set total_limit={} where id=1",(new_limit))
    con.commit()
    con.close()

def get_budget():
    con=sp.connect(database)
    cur=con.cursor()
    cur.execute("select total_limit from budget where id=1")
    rs=cur.fetchone()
    con.close()
    return rs[0] if rs else 0.0


