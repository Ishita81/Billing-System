from sys import stderr
from typing import List
from product import Product, Stock_Product
import display

P_ID_TABLE = "p_id"
STOCK_TABLE = 'stock'

def entry(cnx) -> None:
    display.subheading("Perform Stock Entry")

    # Define MIN_ID
    MIN_ID = 10001
    
    # Create cursor object
    cursor = cnx.cursor()

    # Fetch the last row from the table
    cursor.execute(f"SELECT `id` from `{P_ID_TABLE}` ORDER BY `id` DESC LIMIT 1")
    row = cursor.fetchone()

    # Assign `id` to the new product
    if row:
        p = Stock_Product(row[0] + 1)
    else:
        p = Stock_Product(MIN_ID)

    # Input data into the object
    p.add()

    # Insert data into the database
    cursor.execute(f"INSERT INTO `{P_ID_TABLE}` "
                   f"VALUES ({p.get_id()})")
    cursor.execute(f"INSERT INTO `{STOCK_TABLE}` "
                   f"VALUES ({p.get_id()}, '{p.get_desc()}', {p.get_qty()}, "
                   f"{p.get_MRP()}, {p.get_price()}, {p.get_GST()}, "
                   f"'{p.get_last_updated()}', {p.get_initial_qty()})")

    # Commit the changes to the database
    cnx.commit()

    # Close the cursor()
    cursor.close()

    input("\nPress Enter to continue : ")

def search_product(cnx, suppress_subheading: bool = False) -> List[Product]:
    if not suppress_subheading:
        display.subheading("Search Product")

    # Input search string
    to_search = input("\nEnter Product ID or Description : ")
    
    # Create cursor object
    cursor = cnx.cursor()

    # Search the database for the specified product
    if to_search.isdigit():
        to_search = int(to_search)
        cursor.execute(f"SELECT `id`, `desc`, `qty`, `MRP`, `price`, `GST` from `{STOCK_TABLE}` "
                       f"WHERE `id` = {to_search}")
    else:
        cursor.execute(f"SELECT `id`, `desc`, `qty`, `MRP`, `price`, `GST` from `{STOCK_TABLE}` "
                       f"WHERE `desc` like '%{to_search}%' LIMIT 10")

    rows = cursor.fetchall()
    result = []

    if rows:
        if len(rows) > 1:
            style = "tabular"

            # Display table header
            display.table_header(("Product ID", 10), ("Description", 36), ("Qty", 6),
                                 ("MRP", 9), ("Price", 9), ("GST", 5))
        else:
            style = "stacked"

        for row in rows:
            p = Product(id = row[0], desc = row[1], qty = row[2],
                        MRP = float(row[3]), price = float(row[4]), GST = row[5])
            result.append(p)
            p.print(style)
    else:
        print("No products matching the specified criteria were found.", file = stderr)
        
    # Close the cursor
    cursor.close()

    if not suppress_subheading:
        input("\nPress Enter to continue : ")

    return result

def select_product(results: List[Product], message: str):
    if results:
        if len(results) == 1:
            num = 1
        else:
            while True:
                try:
                    num = int(input(message + f" (1-{len(results)})" + " : "))

                    if num < 1 or num > len(results):
                        raise ValueError
                
                except ValueError:
                    print("Invalid selection. Please try again.", file = stderr)
                    continue
                else:
                    break

        return (p := results[num - 1])
    else:
        return None

def update_entry(cnx) -> None:
    display.subheading("Update Stock Entry")

    # Search and select the entry to be updated
    results = search_product(cnx, True)
    
    if p := select_product(results, "\nSelect the entry to be updated"):
        # Create instance of class `product.Stock_Product`
        sp = Stock_Product(id = p.get_id(), desc = p.get_desc(), qty = p.get_qty(),
                           MRP = p.get_MRP(), price = p.get_price(), GST = p.get_GST())
        
        # Modify data
        if sp.modify():
            # Create cursor object
            cursor = cnx.cursor()

            ts_updated = sp.get_initial_qty() != 0

            # Update the correspnding entry in the database
            cursor.execute(f"UPDATE `{STOCK_TABLE}` " +
                           f"SET `desc` = '{sp.get_desc()}', `qty` = {sp.get_qty()}" +
                           f", `MRP` = {sp.get_MRP()}, `price` = {sp.get_price()}" +
                           f", `GST` = {sp.get_GST()}" +
                           (f", `last_updated` = '{sp.get_last_updated()}'" if ts_updated else "") +
                           (f", `initial_qty` = {sp.get_initial_qty()}" if ts_updated else "") +
                           f" WHERE `id` = {p.get_id()}")
            
            # Commit the changes to the database
            cnx.commit()

            # Print success message
            print("Stock Entry Updated")

            # Close the cursor()
            cursor.close()

    input("\nPress Enter to continue : ")

def delete_product(cnx) -> None:
    display.subheading("Delete Product")

    # Search and select the product to be deleted
    results = search_product(cnx, True)
    
    if p := select_product(results, "\nSelect the product to be deleted"):
        print("\nThe selected product will be deleted.")

        # Create cursor object
        cursor = cnx.cursor()

        # Delete the specified element
        cursor.execute(f"DELETE FROM `{STOCK_TABLE}` "
                       f"WHERE id = {p.get_id()}")
    
        # Commit the changes to the database
        cnx.commit()

        # Close the cursor()
        cursor.close()

    input("\nPress Enter to continue : ")

def list_products(cnx) -> None:
    display.subheading("List All Products")
    
    # Create cursor object
    cursor = cnx.cursor()

    # Fetch all the rows of the table
    cursor.execute(f"SELECT * from `{STOCK_TABLE}`")
    rows = cursor.fetchall()

    # Print all the rows
    if rows:
        # Print table header
        display.table_header(("Product ID", 10), ("Description", 36), ("Qty", 6),
                             ("MRP", 9), ("Price", 9), ("GST", 5))

        for row in rows:
            p = Stock_Product(id = row[0], desc = row[1], qty = row[2],
                              MRP = row[3], price = row[4], GST = row[5],
                              last_updated = row[6], initial_qty = row[7])
            p.print()
    else:
        print("\nNo Records Exist")
    
    # Close the cursor
    cursor.close()

    input("\nPress Enter to continue : ")
