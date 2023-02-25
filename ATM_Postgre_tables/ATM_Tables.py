import psycopg2 


def Create_Tables():   
    hostname= 'localhost'
    database= 'ATM_db'
    username = 'postgres'
    pwd= '1234'
    port_id = '5432'

    conn=psycopg2.connect(
                                host= hostname,
                                dbname =database,
                                user=username,
                                password= pwd,
                                port = port_id)
    cur=conn.cursor()
    command_1= ''' CREATE TABLE IF NOT EXISTS TblCustomer 
    (
                    Customer_id serial PRIMARY KEY,  
                    First_name varchar(20) NOT NULL,
                    Last_name varchar(20) NOT NULL,
                    Email varchar(255) NOT NULL,
                    Password varchar(20) NOT NULL,
                    Create_date timestamp NOT NULL ,
                    Login_log varchar(255),
                    Withdraw_money money,
                    Insert_money money,
                    Transfer_money money,
                    Balance money 
    )
    '''

    command_2 = ''' CREATE TABLE IF NOT EXISTS TblEmployee
    (
        Employee_id serial  PRIMARY KEY,
        Password varchar(10) NOT NULL,
        Customer_id int,
        CONSTRAINT FK_CustomerTblEmployee FOREIGN KEY(Customer_id)  REFERENCES TblCustomer(Customer_id)
        
    )
        '''
    command_3 = ''' CREATE TABLE IF NOT EXISTS TblDailyAktivities
    (               
                    Customer_id int,
                    Employee_id int,
                    TotalMoney money,
                    DailyWithdraw money,
                    DailyInsert money,
                    CONSTRAINT FK_Employee_id_TblDailyAktivities FOREIGN KEY(Employee_id) REFERENCES TblEmployee(Employee_id),
                    CONSTRAINT FK_CustomerTblDailyAktivities FOREIGN KEY(Customer_id)  REFERENCES TblCustomer(Customer_id)


    )
    '''
# database den bu tablolari kaldirmak isterseniz bu seiralamada tam tersinden baslamalisiniz!...
    cur.execute(command_1)
    cur.execute(command_2)
    cur.execute(command_3)
    cur.close()
    conn.commit()
    conn.close()

    
Create_Tables()



# cur=conn.cursor()
# cur.execute(command_2)
# cur.close()
# conn.commit()
# conn.close()
