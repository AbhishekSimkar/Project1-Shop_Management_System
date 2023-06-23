import mysql.connector as con
mydb=con.connect(host='localhost',user='root',passwd='',\
                 database='import_items')
mycursor=mydb.cursor()

mycursor.execute('select name_of_item,quantity \
from entry group by name_of_item having quantity<=2')

stocklist=[]
def stock():
      for i in mycursor:
            stocklist.append(i)
      if len(stocklist)==0:
            print('All Items Are More Than 2.')
      else:
            print('Name Of Item Less Than 3 In Stock Are : ')
            print(stocklist)
