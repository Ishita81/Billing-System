from sys import stderr
import mysql.connector
from mysql.connector import errorcode

# Define the class `customer`
class Customer:
    def __init__(self, mobile_no: int, name: str = '', address: str = '',
                 email: str = '', dues: float = 0) -> None:
        
        # Primary key
        self.__mobile_no = mobile_no

        self.__name = name
        self.__address = address
        self.__email = email
        self.__dues = dues

    def get_mobile_no(self) -> int:
        return self.__mobile_no
    
    def get_name(self) -> str:
        return self.__name
    
    def get_address(self) -> str:
        return self.__address
    
    def get_email(self) -> str:
        return self.__email
    
    def get_dues(self) -> float:
        return self.__dues
    
    def add(self):
        while True:
            try:
                self.__name = input("\nEnter Name of Customer : ")
                self.__address = input("Enter Address : ")
                self.__email = input("Enter Email : ")

                if not ('@' in self.__email and '.' in self.__email):
                    raise ValueError

            except ValueError:
                print("\nInvalid value(s). Please try again.", file = stderr)
                continue
            else:
                break

    def modify(self) -> bool:
        # Print the current details of the customer
        self.print()

        element = input("\nChange (N)ame | (M)obile No. | (E)mail | (A)ddress : ")
        
        while True:
            try:
                if element == 'n' or element == 'N':
                    self.__name = input("\nEnter New Customer Name : ")
                elif element == 'm' or element == 'M':
                    self.__mobile_no = int(input("\nEnter New Mobile No. : "))

                    if not (self.__mobile_no >= 1000000000 and self.__mobile_no <= 9999999999):
                        raise ValueError
                
                elif element == 'a' or element == 'A':
                    self.__address = input("\nEnter New Address : ")
                elif element == 'e' or element == 'E':
                    self.__email = input("\nEnter New Email : ")

                    if not ('@' in self.__email and '.' in self.__email):
                        raise ValueError
                
                else:
                    print("Invalid Selection", file = stderr)
                    return False
                
            except ValueError:
                print("Invalid value. Please try again.", file = stderr)
                continue
            else:
                break

        return True
    
    def print(self):
        print(f"\nName of Customer : {self.__name}")
        print(f"Mobile Number : {self.__mobile_no}")
        print(f"Email: {self.__email}")
        print(f"Address : {self.__address}")

TABLE_NAME = "customers"

def search(cnx) -> Customer:
    # Input Mobile No.
    while True:
        try:
            mobile_no = int(input("\nEnter Mobile No. of Customer : "))

            if not (mobile_no >= 1000000000 and mobile_no <= 9999999999):
                raise ValueError

        except ValueError:
            print("Invalid Mobile Number. Please try again.", file = stderr)
            continue
        else:
            break

    # Create cursor object
    cursor = cnx.cursor()

    # Search the customer in the database
    cursor.execute(f"SELECT * from `{TABLE_NAME}` "
                   f"WHERE `mobile_no` = {mobile_no}")
    row = cursor.fetchone()
    
    if row:
        c = Customer(mobile_no = mobile_no, name = row[1], address = row[2],
                     email = row[3], dues = row[4])
    else:
        c = Customer(mobile_no = mobile_no)
        print("\nThe customer needs to be registered before generating the bill.")
        c.add()

        # Insert data into the table
        cursor.execute(f"INSERT INTO `{TABLE_NAME}` "
                       f"VALUES ({c.get_mobile_no()}, '{c.get_name()}', '{c.get_address()}', "
                       f"'{c.get_email()}', {c.get_dues()})")
        
        # Commit the changes to the database
        cnx.commit()

    # Close the cursor
    cursor.close()

    return c

def modify(cnx, c: Customer) -> None:
    prev_mobile_no = c.get_mobile_no()

    # Create cursor object
    cursor = cnx.cursor()

    # Modify data and them update the corresponding entry in the database
    if c.modify():
        try:
            cursor.execute(f"UPDATE `{TABLE_NAME}` "
                           f"SET `mobile_no` = {c.get_mobile_no()}, `name` = '{c.get_name()}',"
                           f" `address` = '{c.get_address()}', `email` = '{c.get_email()}' "
                           f"WHERE `mobile_no` = {prev_mobile_no}")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("This mobile number belongs to another customer.", file = stderr)
        else:
            print("Customer Details Modified")

    # Commit the changes to the database
    cnx.commit()

    # Close the cursor
    cursor.close()
