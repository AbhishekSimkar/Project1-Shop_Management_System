import mysql.connector as con
import sys
import matplotlib.pyplot as plt
sys.path.append('C:\python\project SAS')
mydb=con.connect(host='localhost',user="root",passwd='',database='import_items')
mycursor=mydb.cursor()
mycursor.execute('select * from entry')
mydb.commit
name=[]
quantity=[]
gst=[]
def plot():
      for i in mycursor:
            name.append(i[1])
            quantity.append(i[3])
      plt.title("---: BAR GRAPH OF STOCK :---",color='m')
      myplot=plt.bar(name,quantity,width=0.5,color=['r','b'])
      ax=plt.axes()
      ax.set_facecolor('pink')
      plt.xlabel("NAME OF ITEM ",color='g')
      plt.ylabel("QUANTITY",color='g')
      plt.show()
def pie():
      for i in mycursor:
            name.append(i[1])
            quantity.append(i[3])
      plt.title("---: PIE CHART OF STOCK :---",color='c')
      plt.pie(quantity,autopct='%1.1f%%',labels=name,\
              colors=['r','g','b','m','c','y'],shadow=True)
      plt.show()
def vis():
      for i in mycursor:
            name.append(i[1])
            gst.append(i[4])
      plt.title("---: TO ANALYS GST OF ITEMS :---",color='m')
      plt.bar(name,gst,width=0.5)
      ax=plt.axes()
      ax.set_facecolor('black')
      plt.xlabel("NAME OF ITEM ",color='g')
      plt.ylabel("GST OF ITEM ",color='g')
      plt.show()
def plot1():
      for i in mycursor:
            name.append(i[1])
            quantity.append(i[3])
      plt.title("---: LINE GRAPH OF STOCK :---",color='m')
      plt.xlabel('NAME OF ITEM',color='g')
      plt.ylabel('QUANTITY',color='g')
      plt.plot(name,quantity,'m',linewidth=2,marker='p',\
               markeredgecolor='k')
      plt.legend()
      plt.show()
