import psycopg2 

class ATM_Table_Create():
    def __init__(self) -> None:  

        self.hostname= 'localhost'
        self.database= 'ATM_db'
        self.username = 'postgres'
        self.pwd= '1234'
        self.port_id = '5432'
        self.customer_table="TblCustomer"
        self.employee_table="TblEmployee"
        self.dailyActivities_table="TblDailyAktivities"

        self.conn=psycopg2.connect(
                            host= self.hostname,
                            dbname =self.database,
                            user=self.username,
                            password= self.pwd,
                            port = self.port_id
                            )
        self.cur=self.conn.cursor()
        

        print("You are connected to the database...")
        print("You cursor was also urgent now ...")
        self.Create_Tables()
       
    def Create_Tables(self):
        self.command_1= ''' CREATE TABLE IF NOT EXISTS tblcustomer 
    (
                    customer_id serial PRIMARY KEY,
                    first_name varchar(20) NOT NULL,
                    last_name varchar(20) NOT NULL,
                    email varchar(255) NOT NULL,
                    password varchar(20) NOT NULL,
                    create_date date NOT NULL DEFAULT CURRENT_DATE  ,
                    login_log varchar(255) DEFAULT CURRENT_DATE,
                    withdraw_money money DEFAULT '00000',
                    insert_money money DEFAULT '00000',
                    transfer_money money DEFAULT '00000',
                    balance money DEFAULT '00000'
    )
    '''
        self.command_2 = ''' CREATE TABLE IF NOT EXISTS tblemployee
    (
        employee_id serial  PRIMARY KEY,
        password varchar(10) NOT NULL,
        customer_id int,
        CONSTRAINT FK_CustomerTblEmployee FOREIGN KEY(customer_id)  REFERENCES tblcustomer(customer_id)
        
    )
        '''

        self.command_3 = ''' CREATE TABLE IF NOT EXISTS tbldailyaktivities
    (               
                    customer_id int,
                    employee_id int,
                    totalMoney money,
                    dailywithdraw money,
                    dailyInsert money,
                    CONSTRAINT FK_Employee_id_TblDailyAktivities FOREIGN KEY(employee_id) REFERENCES tblemployee(employee_id),
                    CONSTRAINT FK_CustomerTblDailyAktivities FOREIGN KEY(customer_id)  REFERENCES tblcustomer(customer_id)


    )
    '''
# If you want to remove these tables from the database, you should start from the reverse in this order!...
        self.cur.execute(self.command_1)
        self.cur.execute(self.command_2)
        self.cur.execute(self.command_3)
        self.cur.close()
        self.conn.commit()
        self.conn.close()
        
        print("Your database connection has been closed")
        print("3 tables were created in ATM_db.")



class Query_open():
        
    customer_table="tblcustomer"
    employee_table="tblemployee"
    dailyActivities_table="tbldailyaktivities"

    def __init__(self) -> None: 
        
        self.hostname= 'localhost'
        self.database= 'ATM_db'
        self.username = 'postgres'
        self.pwd= '1234'
        self.port_id = '5432'
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

    def Query_close(self):

        self.cur.close()
        self.conn.commit()
        self.conn.close()
        print("Your database connection has been closed")
        print("You have to create an object again.")

#customer verilerini islemek icin bu foks ile donderdik.
    def Query_tblcustomer(self):
            
        self.command = f'SELECT * FROM {Query_open.customer_table}'
        self.cur.execute(self.command)
        result =self.cur.fetchall()
        self.Query_close()
        
        return result
    

    def Query_tblemployee(self,d):
        self.command = f'SELECT * FROM {Query_open.employee_table}'
        self.cur.execute(self.command)
        result =self.cur.fetchall()
        self.Query_close()

        return result

    def Query_tbldailyaktivities(self):
        self.command = f'SELECT * FROM {Query_open.dailyActivities_table}'
        self.cur.execute(self.command)
        result =self.cur.fetchall()
        self.Query_close()

        return result
    

    def Insert_tblcustomer(self,*args):
        self.command = f'INSERT INTO tblcustomer (customer_id,first_name,last_name,email,password,create_date) VALUES ({args}) '
        self.cur.execute(self.command)
        print("basari ile insert yapildi..")
        
        self.Query_close()
        
    
    def Update_tblcustomer(self):
        pass



# db_Table=ATM_Table_Create()
#

# qr=Query_open()
# data=qr.Query_tblcustomer()
# print(data)
#
# data=qr.Query_tblemployee()
# print(data)
#
# data=qr.Query_tbldailyaktivities()
# print(data)
#
# qr.Insert_tblcustomer('Ahmet','Oduncu','oduncu@gmail.com','123456') # yazim hatasi veriyor

#