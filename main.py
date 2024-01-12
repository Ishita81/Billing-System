from sys import stderr
from getpass import getpass
import db
import display
import stock
import sales
import analytics

# Input password for accessing the database
password = getpass(prompt = 'Enter password : ')

# Connect to the database
db = db.db(password)
db.connect()

if db.cnx and db.cnx.is_connected():

    # Initialize the tables
    db.initialize_tables(insert_sample_data = "y")

    # Dashboard
    display.heading()

    while True:
        display.subheading("Stock Options")
        print("Perform Stock Entry (1)")
        print("Update Stock Entry (2)")
        print("Search Product (3)")
        print("Delete Stock Entry (4)")
        print("List All Products (5)")
        display.subheading("Bill Generation and Analytics")
        print("Generate Bill (6)")
        print("Show Analytics (7)")
        display.subheading("Other Option(s)")
        print("Quit (0)")

        try:
            opt = int(input("\nSelect an Option : "))
        except ValueError:
            print("Invalid option. Please try again.", file = stderr)
        else:
            
            if opt in range(0, 8):
                if opt == 0:
                    break
                elif opt == 1:
                    stock.entry(db.cnx)
                elif opt == 2:
                    stock.update_entry(db.cnx)
                elif opt == 3:
                    stock.search_product(db.cnx)
                elif opt == 4:
                    stock.delete_product(db.cnx)
                elif opt == 5:
                    stock.list_products(db.cnx)
                elif opt == 6:
                    sales.generate_bill(db.cnx)
                elif opt == 7:
                    analytics.show(db.cnx)
            else:
                print("Invalid option. Please try again.", file = stderr)

    # Terminate the connection to the database
    db.disconnect()
