import mysql.connector as con
mydb=con.connect(host='localhost',user='root',passwd='',database='import_items')
mycursor=mydb.cursor()
def gstitemlist():
        print('(name_of_item,gst_tax)')
        print(' ')
        mycursor.execute('select name_of_item,gst_tax from entry')
        for i in mycursor:
                print(i)
