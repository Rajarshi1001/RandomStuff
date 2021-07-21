import sqlite3
from employee import Employee

# to create a database that lives in RAM that is every time you run the python3 file, the database is created from fresh start.
conn = sqlite3.connect(':memory:')
# to create a permanent database use this connection method instead 
#conn= sqlite3.connect('sample.db')
cursor = conn.cursor()# cursor created for excuting sqlite commands. Sqlite is available under the standard library of python3
cursor.execute("""CREATE TABLE employees (first TEXT,
                  last TEXT, pay INTEGER)""")

def insert_emp(em):
    with conn:
       cursor.execute("INSERT INTO employees VALUES (?,?,?)",(em.first,em.last,em.pay))  
def serachem(lastname):
    cursor.execute("SELECT * FROM employees WHERE last=:last",{'last':lastname})  
    return cursor.fetchall()  
def deleteem(em):
    with conn:
        cursor.execute("DELETE FROM employees WHERE first=:first AND last=:last",{'first':em.first,'last':em.last})    
def updateem(em, pay):
    with conn:
        cursor.execute("""UPDATE employees SET pay=:pay
        WHERE first=:first AND last=:last""",{
    'first':em.first, 'last':em.last, 'pay':pay
})

em1 = Employee("Sourav","Chakroborty",30000)
em2 = Employee("Arunava", "Das", 35000)

insert_emp(em1)
insert_emp(em2)
e = serachem(em1.last)
print(e)
updateem(em1,60000)
e1 = serachem(em1.last)
print(e1)
conn.close()