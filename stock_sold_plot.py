import mysql.connector as con
import sys
import matplotlib.pyplot as plt
sys.path.append('C:\python\project SAS')
mydb=con.connect(host='localhost',user="root",passwd='',database='import_items')
code=[]
code1=[]
quantity=[]
quantity1=[]
def my1():
    mycursor1=mydb.cursor()
    mycursor1.execute('select * from entry')
    mydb.commit
    for i in mycursor1:
        code.append(i[0])
        quantity.append(i[3])
def my2():
    mycursor2=mydb.cursor()
    mycursor2.execute('select * from sell')
    mydb.commit
    for i in mycursor2:
        code1.append(i[0]+0.2)
        quantity1.append(i[3])
def dif():
    my1()
    my2()
    plt.title("---: DIFFERNTIATING BAR GRAPH OF STOCK AND SOLD ITEMS :---",color='b')
    plt.bar(code,quantity,width=0.5,color='r',label='IN STOCK')
    plt.bar(code1,quantity1,width=0.5,color='g',label='SOLD GOODS')
    plt.legend()
    plt.xlabel("ITEM CODE",color='b')
    plt.ylabel("QUANTITY",color='b')
    plt.show()
def dif1():
    my1()
    my2()
    plt.title("---: DIFFERNTIATING LINE GRAPH OF STOCK AND SOLD ITEMS :---",color='b')
    plt.plot(code,quantity,'g',linewidth=2,label='IN STOCK')
    plt.plot(code1,quantity1,'m',linewidth=2,label='SOLD GOODS')
    plt.legend()
    plt.xlabel("ITEM CODE",color='b')
    plt.ylabel("QUANTITY",color='b')
    plt.show()
