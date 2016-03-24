'''
Created on Jan 19, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

import sqlite3 as lite
import sys 

con = None

try:
    con = lite.connect('test.db')
    cur = con.cursor()
    """
    #cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
    con.commit()
    
    car = 'Ferrari2'
    
    
    cur.execute("INSERT INTO Cars VALUES(11, '%s', 7349)" % car )
    con.commit()
    """
    cur.execute("SELECT * FROM Cars")
    
    rows = cur.fetchall()
    
    print rows[1]
    
    
    
    for row in cur.execute("SELECT * FROM Cars ORDER BY Price"):
        print row
    print "\n\n---------------\n"
    
    for row in rows:
        print "Make: ", row[1],"Price: ", row[2] 
        print row[2]
        #print row
        
    #sql = """ DELETE FROM Cars WHERE Id = 11 """
    
    sql = """ DELETE FROM Cars WHERE Name = 'Ferrari' """
    
    cur.execute(sql)
    con.commit()
        
except lite.Error, e:
    print "Error %s " % e.args[0]
    sys.exit(1)
finally:
    if con:
        con.close()
      
    
    