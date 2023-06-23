import mysql.connector as con
mydb=con.connect(host='localhost',user='root',passwd='',\
                 database='import_items')
mycursor=mydb.cursor()
def selling():
      while True:
            choice=input('Press "yes" To Continue\
 Else Press Other Key To Break : ')

            if choice=='yes':
                  name=input('Enter Selled Item Name : ')
                  sr=int(input('Enter The Serial Number : '))
                  price=int(input('Enter The Selled \
Price Of Item Per Piece : '))
                  quantity1=int(input('Enter The Selled Quantity : '))
                  arguments=(sr,name,price,quantity1)
                  values='insert into sell values(%s,%s,%s,%s)'
                  mycursor.execute(values,arguments)
                  mydb.commit
                  mycursor.execute('update entry set \
quantity=quantity-%s \
where name_of_item=%s',(quantity1,name))
                  mydb.commit
            else:
                  break
def buyed():
      mycursor.execute('select * from sell')
      for i in mycursor:
          print(i)
