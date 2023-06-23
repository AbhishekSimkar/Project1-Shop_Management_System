import mysql.connector as con
mydb=con.connect(host='localhost',user='root',passwd='',\
                 database='import_items')
mycursor=mydb.cursor()
def new_entry():
      while True:
            choice=input('Press "no" To Break\
 Else Press Other Key To Continue : ')
            if choice=='no':
                  break
            else:
                  name=input('Enter Item Name : ')
                  code=int(input('Enter Item Code : '))
                  price=int(input('Enter The Price Of \
 Item Per Piece : '))
                  quantity=int(input('Enter The Quantity : '))
                  gst=(price*18)/100
                  arguments=(code,name,price,quantity,gst)
                  values='insert into entry values(%s,%s,%s,%s,%s)'
                  mycursor.execute(values,arguments)
                  mydb.commit()
def update_entry():
      mydb=con.connect(host='localhost',user='root',passwd='',\
                 database='import_items')
      mycursor=mydb.cursor()
      while True:
            choice=input('Press "no" To Break\
 Else Press Other Key To Continue : ')
            if choice=='no':
                  break
            else:
                  name=input('Enter Item Name From Table Entry : ')
                  quantity1=int(input('Enter The Quantity Of \
Item : '))
                  mycursor.execute('update entry set quantity=quantity+%s where name_of_item=%s',(quantity1,name))
                  mydb.commit()
def itemlist():
      print('Items Available In Our Shop ')
      print('(Code,Name Of Item,Price Per Piece,Quantity,Gst)')
      print(' ')
      mycursor.execute('select * from entry')
      for i in mycursor:
            print(i)
