
import psycopg2

# CREATE DATABASE cannot run inside a transaction block to fix your mistake
# self.auto_commit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
#   self.conn.set_isolation_level(self.auto_commit)
#You should use these codes, you can see them below.
from psycopg2 import connect, extensions  




#WORKING WITH POSTGRESQL



class ATM_Create():
    def __init__(self) :  

        self.hostname= 'localhost'
        self.username = 'postgres'
        self.pwd= '1234'
        self.port_id = '5432'
      
        self.auto_commit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        self.conn=psycopg2.connect(
                            host= self.hostname,
                            user=self.username,
                            password= self.pwd,
                            port = self.port_id
                            )
        
        self.conn.set_isolation_level(self.auto_commit)

        self.cur=self.conn.cursor()
        
        self.command_0= '''
                            CREATE DATABASE  atm_db
                            WITH
                            OWNER = postgres
                            
                            ENCODING = 'UTF8'
                            LC_COLLATE = 'C'
                            LC_CTYPE = 'C'
                            TABLESPACE = pg_default
                            CONNECTION LIMIT = -1
                            IS_TEMPLATE = False;
                        '''
                            
        try:
                                                
            self.cur.execute(self.command_0)
            self.cur.close()
            self.conn.commit()
            self.conn.close()
            print(" Your atm_db database has been created...\n\n")

        except :
            print(f"atm_db Database already exists")

        
        
        self.Create_Tables()


    
    #this class automatically creates 3 tbls. 
    def Create_Tables(self):

        self.hostname= 'localhost'
        self.database= 'atm_db'
        self.username = 'postgres'
        self.pwd= '1234'
        self.port_id = '5432'
     

        self.conn=psycopg2.connect(
                            host= self.hostname,
                            dbname =self.database,
                            user=self.username,
                            password= self.pwd,
                            port = self.port_id
                            )
        self.cur=self.conn.cursor()
        

        print("CONNETION SUCCESSFUL..\n\n")
        print("You cursor was also urgent now ...")

        self.command_1= ''' CREATE TABLE IF NOT EXISTS tblcustomer 
    (
                    customer_id int PRIMARY KEY,
                    first_name varchar(20) NOT NULL,
                    last_name varchar(20) NOT NULL,
                    email varchar(255) NOT NULL,
                    balance int ,
                    password varchar(20) NOT NULL,
                    create_date date NOT NULL DEFAULT CURRENT_DATE  
                    
    )
    '''
        self.command_2 = ''' CREATE TABLE IF NOT EXISTS tblemployee
    (
        employee_id serial  PRIMARY KEY,
        password varchar(10) NOT NULL
        
        
    )
        '''

        self.command_3 = ''' CREATE TABLE IF NOT EXISTS tbldailyaktivities
    (               
                    day_id date PRIMARY KEY NOT NULL DEFAULT CURRENT_DATE,
                    totalMoney int,
                    dailywithdraw int,
                    dailyInsert int
                    


    )
    '''
        self.command_4 = ''' CREATE TABLE IF NOT EXISTS tblaccountaktivities
    (               
                    activities_id serial PRIMARY KEY,
                    customer_id int ,
                    balance int,
                    login_log timestamp with time zone DEFAULT CURRENT_TIMESTAMP ,
                    withdraw_money int ,
                    insert_money int  ,
                    transfer_money int
                    
                    


    )
    '''
        

    
    
        


# If you want to remove these tables from the database, you should start from the reverse in this order!...
        self.cur.execute(self.command_1)
        # self.cur.execute(f'ALTER SEQUENCE "tblcustomer_customer_id_seq" RESTART WITH {10000};')
        self.cur.execute(self.command_2)
        self.cur.execute(self.command_3)
        self.cur.execute(self.command_4)
        self.cur.close()
        self.conn.commit()
        self.conn.close()
        
        print("Your database connection has been closed")
        print("4 tables were created in atm_db.\n\n")



class Query_open():
    
    def __init__(self) : 
        
        self.hostname= 'localhost'
        self.database= 'atm_db'
        self.username = 'postgres'
        self.pwd= '1234'
        self.port_id = '5432'

        #With this method, we connect to our db.
        self.Open_host() 


    def Open_host(self):
   
        self.conn=psycopg2.connect(
                            host= self.hostname,
                            dbname =self.database,
                            user=self.username,
                            password= self.pwd,
                            port = self.port_id
                            )
        self.cur=self.conn.cursor()
        print("You are connected to the database...")
        print("You cursor was also urgent now with Query_open ... ")


    #With this method, we close the connection from our db and our transactions are recorded.
    def Query_close(self):

        self.cur.close()
        self.conn.commit()
        self.conn.close()
        print("\nDatabase werd gesloten")

    #query of tables in db
    def Query_tbl(self,tbl_name):
            
        self.command = f'SELECT * FROM {tbl_name}'
        self.cur.execute(self.command)
        result =self.cur.fetchall()
        self.Query_close()
        
        return result
    
    def Query_tbl_1(self,ist,tbl_name):
            
        self.command = f'SELECT {ist} FROM {tbl_name} '
        self.cur.execute(self.command)
        result =self.cur.fetchall()
        self.Query_close()
        
        return result

    def Insert_tbl(self,table_name,*args):
        self.command = f'INSERT INTO {table_name} (customer_id,first_name,last_name,email,password,balance) VALUES(%s,%s,%s,%s,%s,%s) '
        self.insert_value=(args)
        self.cur.execute(self.command,self.insert_value)
        print("basari ile insert yapildi..")
        
        self.Query_close()
    
        
    def Insert_tbl3(self,tble_name,*args):
        self.command = f'INSERT INTO {tble_name} (employee_id , password) VALUES(%s,%s) '
        self.insert3_value=(args)
        self.cur.execute(self.command,self.insert3_value)
        print('basari ile insert yapildi..')
   
        self.Query_close()
    
    def Update_tbl(self,tbl_name,*vl,**kwargs):
        for key,value in kwargs.items():
            for new_val in self.new_val(vl):
    
                self.command= f'UPDATE {tbl_name} SET {key} =%s  WHERE {key} = {value}'
                self.cur.execute(self.command,new_val)
         
       
        self.Query_close()




db_Table=ATM_Create()   
#

# bu kodlari tablolarin icerigini genel olarak almak icin kullaniyoruz. Fonksiyonun icerisine hangi tablo ismini istiyorsak yazmamiz lazim.
# db= Query_open()
# tbl_listem=db.Query_tbl('tblcustomer')
# for i in tbl_listem:
#     print(i)

# qr=Query_open()
# qr.Insert_tbl3('tblemployee',3,'1234' )
# qr=Query_open()
# qr.Insert_tbl3('tblemployee',4,'1234' )

# db= Query_open()
# tbl_listem=db.Query_tbl_1('password','tblcustomer')
# for i in tbl_listem:
#     print(tbl_listem)

#Bu asagidaki kodlarda foksiyona giden ilk deger tablo ismi digerler ise *Args a gidiyor . id mevcut ise hata aliyoruz.
# qr=Query_open()
# qr.Insert_tbl('tblcustomer',6,'cemile','Can','Can@gmail.com','123') #attention ! Error if customer_id exists

# #update  codes
# qr=Query_open()
# v= (1,'Samil','Kaygan','Kaygan@gmail.com','654321')
# x= {'customer_id':6,'first_name':'Huriye','last_name':'Can','email': 'Can@gmail.com'}
# qr.Update_tbl('tblcustomer',v,x)

# db = Query_open()
# tbl_balance = db.Query_tbl_1('balance', 'tblcustomer')
# for b in tbl_balance:
#     print(b)



