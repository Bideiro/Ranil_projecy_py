import mysql.connector

class dbcont:
    
    def __init__(self, user,passwd):
        self.user = user
        self.passwd = passwd
        self.mydb = mysql.connector.connect(
            host="localhost",
            user= "root",
            passwd= "password",
            database="ranil_proj"
        )
        self.mycursor = self.mydb.cursor()
        
        
        
    def login(self):
        try:
            sql = " SELECT EXISTS (SELECT 1 FROM accounts WHERE Uname = %s AND passcode = %s) AS is_found;"
            val = (self.user, self.passwd)
        except:
            print("invalid credentials")
            return False
        self.mycursor.execute(sql,val)
        res = self.mycursor.fetchone()[0]
        return bool(res)
    
    def get_unit_types(self):
        self.mycursor.execute("SELECT UnitType FROM unit_type ORDER BY UnitTypeID")
        listed = [row[0] for row in self.mycursor]
        return listed
    
    def get_cate_types(self):
        self.mycursor.execute("SELECT Category FROM product_category ORDER BY CategoryID")
        listed = [row[0] for row in self.mycursor]
        return listed
    
    def get_sex(self):
        self.mycursor.execute("SELECT Sex FROM sex ORDER BY SexID")
        listed = [row[0] for row in self.mycursor]
        return listed
    
    def get_id_value(self,value,sex = None):
        if sex != None:
            sql = "SELECT Sex FROM sex WHERE SexID = 1"
            self.mycursor.execute(sql)
            return self.mycursor.fetchone()[0]

        
    def get_user_creds(self, User = None, Passcode = None, colint = None, Fname = None , Lname = None):
        
        if User == None and Passcode == None:
            sql = 'SELECT * FROM accounts'
            self.mycursor.execute(sql)
        elif Fname != None and Lname != None:
            sql = 'SELECT * FROM accounts WHERE Fname = %s AND Lname = %s'
            val = (Fname,Lname)
            self.mycursor.execute(sql,val)
        else:
            sql = 'Select * FROM accounts WHERE Uname = %s AND Passcode = %s'
            val = (User,Passcode)
            self.mycursor.execute(sql,val)
            
        if colint == None:
            print('NO COL NUM SELECTED! Fetching all columns!')
            return self.mycursor.fetchall()[0]
        else:
            return self.mycursor.fetchone()[colint][0]
        
    def get_all_names(self):
        sql = "SELECT Fname,Lname FROM accounts"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def reg_user_protocol(self, LevelID, Uname, Passcode, fname, lname, sex, phono, email, Dhired, Bdate, address,  pos = None):
        sql =" INSERT INTO accounts (LevelID, Uname, Passcode, Fname, Lname, SexID, Phono, Email, Position, HireDate, Birthdate, Address) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        val = (LevelID, Uname, Passcode, fname, lname,sex,phono, email,pos, Dhired, Bdate,address)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
    def reg_prod_protocol(self,Pname, Sprice, Utype , Ctype ,desc = None):
        sql =" INSERT INTO products (ProductName, SellingPrice, Description, QuantityTypeID, ProductTypeID) VALUES (%s, %s,%s ,%s,%s)"
        val = (Pname, Sprice,desc, Utype, Ctype )
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
        
    
        
if __name__ == '__main__':
    
    db =dbcont('admin', 123456)
    
    Ulist =db.get_user_creds(Fname= 'Admin' , Lname= 'Admin')
    
    print (Ulist[4])
    
    
    pass