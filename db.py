from sys import stderr
import mysql.connector
from mysql.connector import errorcode
import dataset

class db:
    def __init__(self, password: str, user: str = 'root') -> None:
        self.__config = {
            'user': user,
            'password': password,
            'host': 'localhost'
        }
        
        self.__DB_NAME = 'billing_system'
        self.__TABLES = {}
        self.cnx = None

        # Description of Tables
        self.__TABLES['customers'] = (
            "CREATE TABLE IF NOT EXISTS `customers` ("
            "  `mobile_no` bigint(10) NOT NULL,"
            "  `name` varchar(25) NOT NULL,"
            "  `address` text(50) NOT NULL,"
            "  `email` varchar(32) NOT NULL,"
            "  `dues` decimal(8, 2) NOT NULL,"
            "  PRIMARY KEY (`mobile_no`)"
            ")")
        
        self.__TABLES['p_id'] = (
            "CREATE TABLE IF NOT EXISTS `p_id` ("
            "  `id` int(5) NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ")")
        
        self.__TABLES['stock'] = (
            "CREATE TABLE IF NOT EXISTS `stock` ("
            "  `id` int(5) NOT NULL,"
            "  `desc` varchar(48) NOT NULL,"
            "  `qty` int(3) NOT NULL,"
            "  `MRP` decimal(8, 2) NOT NULL,"
            "  `price` decimal(8, 2) NOT NULL,"
            "  `GST` int(2) NOT NULL,"
            "  `last_updated` datetime NOT NULL,"
            "  `initial_qty` int(3) NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ")")
        
        self.__TABLES['sales'] = (
            "CREATE TABLE IF NOT EXISTS `sales` ("
            "  `id` int(5) NOT NULL,"
            "  `desc` varchar(48) NOT NULL,"
            "  `qty` int(2) NOT NULL,"
            "  `MRP` decimal(8, 2) NOT NULL,"
            "  `price` decimal(8, 2) NOT NULL,"
            "  `GST` int(2) NOT NULL,"
            "  `bill_no` int(6) NOT NULL,"
            "  `timestamp` datetime NOT NULL"
            ")")
        
        self.__TABLES['bills'] = (
            "CREATE TABLE IF NOT EXISTS `bills` ("
            "  `bill_no` int(6) NOT NULL,"
            "  `mobile_no` bigint(10) NOT NULL,"
            "  `timestamp` datetime NOT NULL,"
            "  `total_items` int(2) NOT NULL,"
            "  `total_qty` int(3) NOT NULL,"
            "  `total_amount` decimal(8, 2) NOT NULL,"
            "  `net_amount` decimal(8, 2) NOT NULL,"
            "  `amount_paid` decimal(8, 2) NOT NULL,"
            "  PRIMARY KEY (`bill_no`)"
            ")")
    
    def connect(self) -> None:
        try:
            # Initialize the connection
            self.cnx = mysql.connector.connect(**self.__config, database = self.__DB_NAME)
        except mysql.connector.Error as err:
            
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid password", file = stderr)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                # Database does not exist
                try:
                    self.cnx = mysql.connector.connect(**self.__config)
                except mysql.connector.Error as err:
                    print("Failed to connect to the database", file = stderr)
                else:
                    # Create cursor object
                    cursor = self.cnx.cursor()

                    # Create new database
                    cursor.execute(f"CREATE DATABASE {self.__DB_NAME}")
                    self.cnx.database = self.__DB_NAME

                    # Close the cursor
                    cursor.close()

            else:
                print(err.msg, file = stderr)
            
    
    def initialize_tables(self, insert_sample_data = "y") -> None:
        if self.cnx and self.cnx.is_connected():
            # Create cursor object
            cursor = self.cnx.cursor()

            # Create tables if they do not exist already
            for table_name in self.__TABLES:
                table_description = self.__TABLES[table_name]
            
                try:
                    cursor.execute(table_description)
                except mysql.connector.Error as err:
                    print(err.msg, file = stderr)

            if insert_sample_data == 'y':
                for table_name in dataset.data:
                    # Check if the table is empty
                    cursor.execute(f"SELECT COUNT(*) FROM `{table_name}`")
                    row = cursor.fetchone()

                    if row and row[0] == 0:
                    # Insert sample data from the dataset
                        insert_query = dataset.data[table_name]
                        cursor.execute(insert_query)
                        self.cnx.commit()

            # Close the cursor
            cursor.close()

    def disconnect(self) -> None:
        # Close the connection
        if self.cnx and self.cnx.is_connected():
            self.cnx.close()
