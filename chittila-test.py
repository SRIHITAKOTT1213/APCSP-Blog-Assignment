#!/usr/bin/env python3

# Assignment 3 - Structured Query Language
# Author:  Lalitha Chittila

import sqlite3
import os
import logging

def debug_config():
    logging.basicConfig(level=logging.DEBUG,format = "[Movies]:%(asctime)s:%(levelname)s:%(message)s") #DEBUG,INFO,ERROR,WARNING,CRITICAL

def db_checkfile(dbfile):
    if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
          logging.debug("{a} found and not zero size".format(a=dbfile))
    else:
          logging.error("{a} not found or zero size".format(a=dbfile))

def db_connect(dbfile):
    con = sqlite3.connect(Movies.db)
    logging.debug("DB Connected".format())
    return con

def db_cursor(con):
    cur = con.cursor()
    logging.debug("Cursor set".format())
    return cur

def db_runquery(cur,query):
    cur.execute(query)
    result = cur.fetchall()
    logging.debug("DB Query executed and returned".format())
    return result

def main():
    dbfile = 'Movies.db'
    programname = "My Movie Database"
    debug_config()
    print(programname)
con = sqlite3.connect('movies2.db')

cur = con.cursor()
#query to select all the elements from the artists table
query = '''CREATE TABLE movies_info_1(
show_id INTEGER PRIMARY KEY AUTOINCREMENT,
genere TEXT,
title TEXT,
director TEXT
)'''

#run the query
cur.execute(query)

#save the results in artists
movies = cur.fetchall()

#cur2=con.cursor()
query1='''CREATE TABLE movies_info_3(
show_id INTEGER
release_year TEXT,
description TEXT,
 CONSTRAINT FK_showid FOREIGN KEY (show_id)
    REFERENCES movies_info_1(show_id)
)'''

#run the query
cur.execute(query1)

#save the results in artists
movies = cur.fetchall()

#cur3=con.cursor()
query2='''insert into movies_info_1
values (1,'Comdey', 'Mrs Doubtfire', 'Chris Columbus')
insert into movies_info_1
values (2,'Comdey', 'My Cousin Vinny', 'Jonathan Lynn')
insert into movies_info_1
values (3,'Children Film', 'Finding Nemo', 'Andrew Stanton')'''

cur.execute(query2)
movies = cur.fetchall()

#cur4.concursor()
query3='''insert into movies_info_2
values(1,'1993','Family Drama'),
(2,'1992','Cousin Bonding')
,(3,'2003','True story in Cartoon form)'''

cur.execute(query3)
movies=cur.fetchall()

query4='''select * from movies_info_1'''
cur.execute(query4)
movies=cur.fetchall()

query5='''select * from movies_info_2'''
cur.execute(query5)
movies=cur.fetchall()

query6='''select * from movies_info_1 as m1
left join movies_info_1 as m2 on mi.show_id=m2.show_id '''
cur.execute(query6)
movies=cur.fetchall()

if con:
    con.close()


db_checkfile(dbfile)
try:
     con = db_connect(dbfile)
     cur = db_cursor(con)
     query = 'SELECT SQLITE_VERSION()'
     res = db_runquery(cur, query )
     print("SQLLITE version: " , res[0][0])
except sqlite3.Error as error:
          logging.error("Error executing query", error)
finally:
     if con:
          con.close()
          logging.debug("[Info] DB Closed".format())
          print('Done - check completed')
          logging.info("Completed.")
     if __name__ == '__main__':
          main()