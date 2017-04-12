import re
import sys
import sqlite3
import codecs
		
#db = Db(sqlite3.connect('dbtest2' + '.db'), Sql())
		

'''
db = sqlite3.connect('dbtest1.db')
cur = db.cursor()

##add data file into database
category = "Sports"
with open("w2_.txt", "r") as sports:
    lines = sports.readlines()

for line in lines:
  # Split the line on whitespace
  data = line.split()
  number = data[0]
  word1 = data[1]
  print data
  cur.execute(INSERT INTO users(person_id, category, type)
			VALUES(?,?,?), (number, category, word1))

db.commit()
db.close()	
		
category = "Sports"
with open("w2_.txt", "r") as sports:
    lines = sports.readlines()

for line in lines:
    # Split the line on whitespace
    data = line.split()
    number = data[0]
    word1 = data[1]
print "end"	'''
############### CREATE DB ##########################
#db = sqlite3.connect('dbtest16.db')
#cursor = db.cursor()
#cursor.execute('''
 #   CREATE TABLE word(word1 TEXT,
 #                      word2 TEXT,word3 TEXT, count INTEGER)''')
#cursor.execute('''
#    CREATE TABLE param(name TEXT,
#                        value INTEGER)''')

					   
#db.commit()
#db.close()
#################INSERT DB #########################
db = sqlite3.connect('dbtest16.db')
cursor = db.cursor()

import codecs

	
with open("w3.txt", "r") as sports:
    lines = sports.readlines()
	
for line in lines:
    # Split the line on whitespace
    data = line.split()
    number = data[0]
    word1 = data[1]
    word2= data[2]
    word3 = data[3]
    name ='depth'
    value = 2
   #print word2
    cursor.execute('''INSERT INTO word(word1,word2,word3,count)
		VALUES(?,?,?,?)''', (word1,word2,word3,number))	
		
    cursor.execute('''INSERT INTO param(name,value)
		VALUES(?,?)''', (name,value))	
#print "end"	
 
db.commit()
db.close()
