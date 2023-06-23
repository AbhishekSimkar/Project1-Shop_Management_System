import mysql.connector as con
import sys
import matplotlib.pyplot as plt
sys.path.append('C:\python\project SAS')
mydb=con.connect(host='localhost',user="root",\
                 passwd='',database='import_items')
mycursor=mydb.cursor()
mycursor.execute('select * from sell')
mydb.commit
name=[]
quantity=[]
def plot():
      for i in mycursor:
            name.append(i[1])
            quantity.append(i[3])
      plt.title("---: BAR GRAPH OF SELL :---",color='m')
      plt.bar(name,quantity,width=0.5,color=['r','b'])
      ax=plt.axes()
      ax.set_facecolor('black')
      plt.xlabel("NAME OF ITEM ",color='g')
      plt.ylabel("QUANTITY",color='g')
      plt.show()
def plot1():
      for i in mycursor:
            name.append(i[1])
            quantity.append(i[3])
      plt.title("---: LINE GRAPH OF SELL :---",color='m')
      plt.xlabel('NAME OF ITEM',color='g')
      plt.ylabel('QUANTITY',color='g')
      plt.plot(name,quantity,'r',linewidth=2,marker='p',\
               markeredgecolor='b',linestyle='dashed')
      plt.legend()
      plt.show()
