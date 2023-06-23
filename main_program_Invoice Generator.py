import sys
sys.path.append('C:\python\project SAS')
import item_entry as enr
import stock_list as stk
import gst_tax as gst
import selled_items as slt
import stock_plot as plt
import sell_plot as splt
import stock_sold_plot as ssplt
print(' '*23+'-'*36)
print('''
                       -: WELCOME TO DRAGON  ELECTRONICS :-
                              ''')
print(' '*23+'-'*36)
while True:
    identity=int(input('     Are You Owner Of Shop Or Costomer?\n \
     Select 1:Owner And \n \
     Select 2:Costumer \n \
     Select 3:For Exit \n \
     Your Choice  :'))
    if identity==1:
        passwd=eval(input('''
     Enter The Password : '''))
        if passwd==1234:
            while True:
                choice=int(input('''
      1:To Enter Data Of New Items  \n \
     2:To See The Scarcity Of Items In Stock \n \
     3:To See The Gst Tax Imposed On Items \n \
     4:To See The Graphs \n \
     5:To Enter name and other information About Item You Want To Sell \n \
     6:To Update The Quantity Of Item \n \
     7:To See The List Of Items In The Shop\n \
     8:To See The Data Of Items You Sold\n \
     9:To Exit The Owner Section \n \
     
     Press Number From 1 To 8 Acccordind To Your Interest : '''))
                if choice==1:
                    print('''
                                -: THE ITEM ENTRY SECTION :-


                          ''')
                    enr.new_entry()
                    continue
                if choice==2:
                    print('''
                                -: THE STOCK SECTION :-
                   
                    ''')
                    stk.stock()
                    continue
                if choice==3:
                    print('''
                               -: THE GST TAXATION SECTION :-

                          ''')
                    gst.gstitemlist()
                    continue
                if choice==4:
                    print('''
                               -: THE VISUALISATION ANALYSIS SECTION :-

                          ''')
                    choice=int(input('''
      1:To See The Bar Graph Of Items In Stock(Quantity) \n \
     2:To See The Bar Graph Of Sold Items(Quantity) \n \
     3:To See The Pie Plot Of Stock \n \
     4:To See The GST Of Items In Stock \n \
     5:To See The Line Graph Of Items In Stock \n \
     6:To See The Line Graph Of Sold Items \n \
     7:To See The Differentiating Bar Graph Of Stock And Sold Items \n \
     8:To See The Differentiating Line Graph Of Stock And Sold Items
      9:To Return Back To Owner Section Homepage \n \
    \n \
     Enter Your Choice : '''))
                    if choice==1:
                        plt.plot()
                        continue
                    if choice==2:
                        splt.plot()
                        continue
                    if choice==3:
                        plt.pie()
                        continue
                    if choice==4:
                        plt.vis()
                        continue
                    if choice==5:
                        plt.plot1()
                        continue
                    if choice==6:
                        splt.plot1()
                        continue
                    if choice==7:
                        ssplt.dif()
                        continue
                    if choice==8:
                        ssplt.dif1()
                        continue
                    if choice==9:
                        print('''
                              -: THANK YOU FOR VISITING VISUALISATION \
                              ANALYSIS SECTION :-
                              ''')
                        break  
                    else:
                        sys.stderr.write('''
            Please!! Enter Number From 1 To 9

                        ''')
                        continue
                if choice==5:
                    print('''
                           -: THE ITEM SELLING SECTION :-

                      ''')
                    slt.selling()
                    continue
                if choice==6:
                    print('''
                               -: THE ITEM ENTRY SECTION :-      

                         ''')
                    enr.update_entry()
                    continue
                if choice==7:
                    print('''
                               -: THE AVAIBILITY SECTION :-   

                          ''')
                    enr.itemlist()
                    continue
                if choice==8:
                    print('''
                               -: THE ITEM SELLING SECTION :-

                          ''')
                    slt.buyed()
                    continue
                if choice==9:
                    print('''
                            -: THANK YOU FOR VISITING OUR OWNER SECTION :-

                         ''')
                    break
                else:
                    sys.stderr.write('''
            Please!! Enter Number From 1 To 9

                  ''')
                    continue
        else:
            sys.stderr.write('''
           Please!! Enter Correct Password

             ''')
            continue
    if identity==2:
        while True:
            choice=int(input('''
\n \
                   Select A Number From Given Optins \n \
                   \n \
     1:To See The List Of Items In The Shop\n \
     2:To See The Gst Imposed On Each Item\n \
     3:To See Purchase \n \
     4:To Exit The Costumer Section \n \
     
     Enter Your Choice : '''))
            if choice==1:
                print('''
                            -: THE AVAIBILITY SECTION :-

                     ''')
                enr.itemlist()
                continue
            if choice==2:
                print('''
                            -: THE GST TAXATION SECTION :-

                     ''')
                gst.gstitemlist()
                continue
            if choice==3:
                print('''
                           -: THE ITEM BORROWING SECTION :-    
                      ''')
                slt.buyed()
                continue
            if choice==4:
                print('''
            -: THANK YOU FOR VISITING OUR COSTUMER SECTION :-

                                 ''')
                break
            else:
                sys.stderr.write('''
               Please!! Select Number From 1 To 7

''')
                continue
    if identity==3:
        print('''
                          -: THANK YOU FOR VISITING DRAGON ELECTRONICS :-

                          ''')
        break
