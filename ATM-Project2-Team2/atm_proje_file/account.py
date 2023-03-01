'''
This is an Atm app that can hold users information and allows them make money activities. 

'''



import random
import psycopg2
from PyQt5.QtWidgets import *
from Ui_account import Ui_accountScreen
from Ui_balance import Ui_balanceScreen 
from Ui_insert import Ui_insertScreen
from Ui_withdraw import Ui_withdrawScreen
from Ui_Change_customer_datails import Ui_MainWindow2
from Ui_transfer import Ui_transfer
from Ui_admin_choice import Ui_MainWindow1
from Ui_See_bank_details import Ui_MainWindow

from Ui_login import Ui_loginScreen
from ui_loginAdmin import Ui_loginAdmin   # for admin
from ui_accountAdmin import Ui_accountAdmin # for admin
from Ui_statement import Ui_statementScreen
import datetime
import time

from Query_db import*

import json
import os

__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

from random import randint, randrange

randint(100, 999)     # randint is inclusive at both ends
randrange(100, 1000)  # randrange is exclusive at the stop

class LoginPage(QMainWindow):
    '''
    login page of the app where user can enter 
    '''
    
    
    def __init__(self):
        super().__init__()
        
        self.loginform = Ui_loginScreen()       
        self.loginform.setupUi(self)
        self.openaccountpage = AccountPage()
        self.loginform.enter_button_2.clicked.connect(self.returnLoginAdmin)
        self.loginform.enter_button.clicked.connect(self.enter)
        self.loginform.id_label2.hide()
    

    def returnLoginAdmin(self):
        self.loginReturnForm= LoginAdminPage()
        self.hide()
        self.loginReturnForm.show()


    def enter(self):
        global user,password
       
        try :
            self.id = int(self.loginform.idnum_edit.text())
            self.password = self.loginform.password_edit.text()
        
            user = int(self.id)
            password = self.password
            

            db= Query_open()
            
            tbl_listem=db.Query_tbl_1('password', 'tblcustomer')
            
            db= Query_open()
            tbl_list=db.Query_tbl_1('customer_id', 'tblcustomer')
            
            
            for i in range(len(tbl_listem)):
                
                if (tbl_listem[i][0]) == self.password and (tbl_list[i][0]== self.id):
                    # db= Query_open()
                    # db.cur.execute(f'INSERT INTO tblaccountaktivities (customer_id) VALUES({user})')
                    self.hide()
                    self.openaccountpage.show()
                else :
                    self.loginform.id_label2.show()
                    self.loginform.id_label2.setText("Wrong name or password !!!")

              
        except :
            self.loginform.id_label2.show()
            self.loginform.id_label2.setText("Wrong name or password !!!")
            
           
                              
                        
    def login_log(self):
        pass
        
    
                          
class AccountPage(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.account_page_form = Ui_accountScreen()
        self.account_page_form.setupUi(self)
        self.account_page_form.check_button.clicked.connect(self.balance)
        self.account_page_form.insert_button.clicked.connect(self.insert)
        self.account_page_form.withdraw_button.clicked.connect(self.withdraw)
        self.account_page_form.statement_button.clicked.connect(self.statement)
        self.account_page_form.return_button.clicked.connect(self.go_login)
        self.account_page_form.btn_edit_info.clicked.connect(self.edit_info)
        self.account_page_form.insert_button_2.clicked.connect(self.transfer)

    def transfer(self):
        self.transferform = Transferpage()
        self.close()
        self.transferform.show()
        
    def edit_info(self):
        self.editform = Editpage()
        self.close()
        self.editform.show()
    
    def go_login(self):
        self.loginform = LoginPage()
        self.close()
        self.loginform.show()

    
         
                    
    def balance(self):
        self.open_balance_page = BalancePage()
        self.hide()
        self.open_balance_page.show()

    def insert(self):
        self.open_insert_page = InsertPage()
        self.hide()
        self.open_insert_page.show()
        



    def withdraw(self):
        self.open_withdraw_page = WithdrawPage()
        self.close()
        self.open_withdraw_page.show()
    def statement(self):
        self.open_statement_page = StatementPage()
        self.close()
        self.open_statement_page.show()

class Transferpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.transfer_money = Ui_transfer()
        self.transfer_money.setupUi(self)
        self.transfer_money.return3_button.clicked.connect(self.donus)
        self.transfer_money.lbl_error_credit.hide()
        self.transfer_money.lbl_error_customerid.hide()
        self.transfer_money.lbl_error_limit.hide()
        self.transfer_money.lbl_error_valid_amount.hide()
        self.transfer_money.lbl_succesfull.hide()

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()

    
class Editpage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editinfo = Ui_MainWindow()
        self.editinfo.setupUi(self)
        self.editinfo.return2_button.clicked.connect(self.donus)

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()

class BalancePage(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.checkbalance = Ui_balanceScreen()
        self.checkbalance.setupUi(self)
        self.checkbalance.return1_button.clicked.connect(self.donus)

        db = Query_open()
        
        db.command = f'SELECT balance FROM tblcustomer where customer_id = {user} '
        db.cur.execute(db.command)
        result =db.cur.fetchall()
        db.Query_close()
        self.checkbalance.balance_label.setText(str(result[0][0]))
        
       

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()
class InsertPage(LoginPage,QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.insert_money = Ui_insertScreen()
        
        self.insert_money.setupUi(self)
        self.insert_money.return2_button.clicked.connect(self.donus)
        self.insert_money.balance3_label.hide()
        
        db = Query_open()
        
        db.command = f'SELECT balance FROM tblcustomer where customer_id = {user} '
        db.cur.execute(db.command)
        result =db.cur.fetchall()
        db.Query_close()
        self.insert_money.balance2_label.setText(str(result[0][0]))
        self.insert_money.enter2_button.clicked.connect(self.add_money)
        print(result[0][0])
            
        

    def add_money(self):

        # try :
            db = Query_open()
            db.command = f'SELECT balance FROM tblcustomer where customer_id = {user} '

            db.cur.execute(db.command)
            result =db.cur.fetchall()
            db.Query_close()
            self.insert_money.balance2_label.setText(str(result[0][0]))
            


            db = Query_open()
            
           
            # db.command= f'UPDATE tblaccountaktivities SET insert_money ={int(self.insert_money.insert_edit.text())}  WHERE customer_id = {user}'
            
            # db.cur.execute(db.command)
            new_balance = int(self.insert_money.insert_edit.text())+ (result[0][0])
            db.cur.execute(f'INSERT INTO tblaccountaktivities (customer_id,balance,insert_money) VALUES({user},{new_balance},{int(self.insert_money.insert_edit.text())}) ')
            
            db.cur.execute(f'UPDATE tblcustomer SET balance ={new_balance}  WHERE customer_id = {user}')
            # db.cur.execute(f'UPDATE tblaccountaktivities SET balance ={new_balance}  WHERE customer_id = {user}')
            
            
            db.Query_close()

            db = Query_open()
            db.command = f'SELECT balance FROM tblcustomer where customer_id = {user} '
            db.cur.execute(db.command)
            result =db.cur.fetchall()
            db.Query_close()
            self.insert_money.balance2_label.setText(str(result[0][0]))
            

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()
    
class WithdrawPage(LoginPage,QMainWindow):
    

    def __init__(self):
        super().__init__()
        self.withdraw_money = Ui_withdrawScreen()
        self.withdraw_money.setupUi(self)
        self.withdraw_money.return3_button.clicked.connect(self.donus)

        
        db = Query_open()
        db.command = f'SELECT balance FROM tblcustomer where customer_id = {user} '
        db.cur.execute(db.command)
        result =db.cur.fetchall()
        db.Query_close()
        self.withdraw_money.balance3_label.setText(str(result[0][0]))
        
        self.withdraw_money.enter_button.clicked.connect(self.take_money)

                    
    def take_money(self):
           

        db = Query_open()
        db.command = f'SELECT balance FROM tblcustomer where customer_id = {user} '

        db.cur.execute(db.command)
        result =db.cur.fetchall()
        db.Query_close()
        self.withdraw_money.balance3_label.setText(str(result[0][0]))
        if int(self.withdraw_money.withdraw_edit.text()) > result[0][0]:
            
            self.withdraw_money.messsage2_button.setText("Insufficient Fund !!!")
        elif  int(self.withdraw_money.withdraw_edit.text()) > 1000:
            self.withdraw_money.messsage2_button.setText("Daily withdraw limit exceeded")

        else :     


            db = Query_open()
            new_insert = int(self.withdraw_money.withdraw_edit.text())
            # db.command= f'UPDATE tblaccountaktivities SET withdraw_money ={new_insert}  WHERE customer_id = {user}'
            # db.cur.execute(db.command)
            new_balance2 = (result[0][0]) - int(self.withdraw_money.withdraw_edit.text())
            db.command= f'UPDATE tblcustomer SET balance ={new_balance2}  WHERE customer_id = {user}'
            db.cur.execute(db.command)
            db.cur.execute(f'INSERT INTO tblaccountaktivities (customer_id,balance,withdraw_money) VALUES({user},{new_balance2},{int(self.withdraw_money.withdraw_edit.text())}) ')
            
            
            db.Query_close()

            db = Query_open()
            db.command = f'SELECT balance FROM tblcustomer where customer_id = {user} '
            db.cur.execute(db.command)
            result =db.cur.fetchall()
            db.Query_close()
            self.withdraw_money.balance3_label.setText(str(result[0][0]))
            self.withdraw_money.messsage2_button.setText("Succesfully withdrawed")
        
      

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()     
class StatementPage(LoginPage,QMainWindow):
    def __init__(self):
        super().__init__()
        self.statement_user = Ui_statementScreen()
        self.statement_user.setupUi(self)
        self.statement_user.return4_button.clicked.connect(self.donus)
        self.statement_user.textBrowser.hide()
        self.statement_user.textBrowser_2.hide()

        db = Query_open()
        tbl_log = db.Query_tbl_1('login_log','tblcustomer')
        for log in tbl_log:
            print(log)
        
        tbl_balance = db.Query_tbl_1('balance', 'tblcustomer')
        for b in tbl_balance:
            
            print(b) 
        
        # with open(os.path.join(__location__, 'data2.json')) as f:
        #     self.data = json.load(f)
        #     a = ''
        #     b = ''
        #     for i in self.data["customers"][int(user)-1]["login_log"]:
        #         a += f"{i} \n"
        #     self.statement_user.logins_label.setText(a)
        #     self.statement_user.date_label.setText(self.data["customers"][int(user)-1]["register_log"])
        #     for i in self.data["customers"][int(user)-1]["money_activities"]:
        #         b += f"{i} \n"
        #     self.statement_user.aktivites_label.setText(b)
        #     # self.statement_user.check_label.setText(str(self.data["customers"][int(user)-1]["balance"])+" $")
            

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()
        


# Admin Screen

class LoginAdminPage(QWidget):  # klas olusturdugumuzda bunu QT designer daki (QWidget) sinifin alt sinifi yapiyoruz.
    def __init__(self) -> None:  
        super().__init__()
        self.loginForm= Ui_loginAdmin()      #bu ve alttaki kod ile nesne yaratip sonra ana modulunu(self ile) cagiriyoruz.
        self.loginForm.setupUi(self)
        self.loginForm.labelErrorMessage.hide()
        self.loginForm.pushButtonLogin.clicked.connect(self.choice_menu)
        self.loginForm.pushButtonLogin.clicked.connect(self.AccountAdminOpen) # login tiklanirsa AccountOpen modulunu calistiracak.
        self.loginForm.pushButtonLogin2.clicked.connect(self.go_customer_login)

    def choice_menu(self):
        self.choiceform = Choicepage()
        self.close()
        self.choiceform.show()


    def go_customer_login(self):
        self.loginform = LoginPage()
        self.close()
        self.loginform.show()

        
     
   
    def AccountAdminOpen(self):
        global user,password
       
        try :
            self.user_id = int(self.loginForm.lineEditUser.text())
            self.user_password = self.loginForm.lineEditPassword.text() 
        
            user = int(self.user_id)
            password = self.user_password
            
    
            db= Query_open()
            user_listm = db.Insert_tbl3('employee_id' , 'tblemployee')
            db= Query_open()
            pass_listm=db.Insert_tbl3('password', 'tblemployee')
            for i in range(len(user_listm)):
                if (user_listm[i][0]) == self.user_password and (pass_listm[i][0]== self.user_password):
                        self.accountForm= AccounAdminPage()
                        self.close()   
                        self.accountForm.show()
                    
                        self.hide()
        except :
            self.loginForm.labelErrorMessage.setText(" User Name or  User Password is incorrect! Try Again ")
            self.loginForm.labelErrorMessage.show()
                




class Choicepage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.choiceform = Ui_MainWindow1()
        self.choiceform.setupUi(self)
        self.choiceform.btn_activities.clicked.connect(self.activities)
        self.choiceform.btn_change.clicked.connect(self.change)
        self.choiceform.btn_register.clicked.connect(self.register)
        self.choiceform.return2_button.clicked.connect(self.return_login)


    def return_login(self):
        self.loginform = LoginAdminPage()
        self.close()
        self.loginform.show()

    def register(self):
        self.accountForm= AccounAdminPage()
        self.close()   
        self.accountForm.show()

    def change(self):
        self.changepage = Changepage()
        self.close()
        self.changepage.show()

    
    def activities(self):
        self.activitypage = Activitypage()
        self.close()
        self.activitypage.show()


from Ui_Change_customer_datails import Ui_MainWindow2


class Changepage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.changeform = Ui_MainWindow2()
        self.changeform.setupUi(self)
        self.changeform.return2_button.clicked.connect(self.return_admin_choice)
    
    def return_admin_choice(self):
        self.choiceform = Choicepage()
        self.close()
        self.choiceform.show()
    



class Activitypage(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.activityform = Ui_MainWindow()
        self.activityform.setupUi(self)
        self.activityform.return2_button.clicked.connect(self.returnLoginAdmin)

    def returnLoginAdmin(self):
        self.choiceform = Choicepage()
        self.close()
        self.choiceform.show()
    

class AccounAdminPage(QWidget):  
    
    def __init__(self) :
        super().__init__()
        
        # ornek ve ana modul calistiriliyor
        self.accounderForm= Ui_accountAdmin()
        self.accounderForm.setupUi(self)
        self.accounderForm.pushButtonReturn.clicked.connect(self.return_admin_choice)
        self.accounderForm.pushButtonSuffix.clicked.connect(self.write_db)
        # self.accounderForm.pushButtonSuffix.clicked.connect(self.accoundCread)
        self.accounderForm.label.hide()


    
                




    def write_db(self):  # bu aşamada database yazılıyr

        

        qr=Query_open()
        customer_id = randint(100000, 999999)
        qr.Insert_tbl('tblcustomer',customer_id,self.accounderForm.lineEditName.text(),self.accounderForm.lineEditSurname.text(),self.accounderForm.lineEditEmail.text(),self.accounderForm.lineEditPassword.text(),self.accounderForm.lineEditBalans.text()) #attention ! Error if customer_id exists
        print(customer_id)
        
        
       

    def return_admin_choice(self):
        self.choiceform = Choicepage()
        self.close()
        self.choiceform.show()