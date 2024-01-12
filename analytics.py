import display

CUSTOMER_TABLE = "customers"
STOCK_TABLE = "stock"
SALES_TABLE = "sales"
BILLS_TABLE = "bills"

def most_valuable_customers(cnx) -> None:
    # Create cursor object
    cursor = cnx.cursor()

    # Get the list of the 10 most valuable customers from the database
    cursor.execute("SELECT C.`mobile_no`, C.`name`, SUM(B.`amount_paid`) "
                   f"FROM {CUSTOMER_TABLE} C "
                   f"JOIN {BILLS_TABLE} B ON C.`mobile_no` = B.`mobile_no` "
                   "GROUP BY C.`mobile_no` "
                   "ORDER BY SUM(B.`amount_paid`) DESC "
                   "LIMIT 10")
    rows = cursor.fetchall()

    if (rows):
        display.table_header(("Mobile No.", 10), ("Name", 25), ("Value Contributed", 17))

        for row in rows:
            print(f"{row[0]: <10}", f"{row[1]: <25}", row[2])
    else:
        print("\nNot Enough Data")

    # Close the cursor
    cursor.close()

def stock_alert(cnx) -> None:
    # Create cursor object
    cursor = cnx.cursor()

    # Get the details of the products whose stock levels are low
    cursor.execute(f"SELECT `id`, `desc`, `qty` FROM {STOCK_TABLE} "
                   "WHERE CAST(`qty` AS FLOAT) / `initial_qty` < 0.2"
                   "ORDER BY CAST(`qty` AS FLOAT) / `initial_qty` "
                   "LIMIT 10")
    rows = cursor.fetchall()
    
    if (rows):
        display.table_header(("Product ID", 10), ("Description", 36), ("Qty Remaining", 13))

        for row in rows:
            print(f"{row[0]: 10}", f"{row[1][:36]: <36}", row[2])
    else:
        print("\nNot Enough Data")

    # Close the cursor
    cursor.close()

def best_selling_products(cnx) -> None:
    # Create cursor object
    cursor = cnx.cursor()

    # Get the details of the best selling products from the database
    cursor.execute(f"SELECT `id`, `desc`, SUM(`qty`) FROM {SALES_TABLE} "
                   "GROUP BY `id`, `desc`"
                   "ORDER BY SUM(`qty`) DESC "
                   "LIMIT 10")
    rows = cursor.fetchall()
    
    if (rows):
        display.table_header(("Product ID", 10), ("Description", 36), ("Qty Sold", 8))

        for row in rows:
            print(f"{row[0]: 10}", f"{row[1][:36]: <36}", row[2])
    else:
        print("\nNot Enough Data")

    # Close the cursor
    cursor.close()

def worst_selling_products(cnx) -> None:
    # Create cursor object
    cursor = cnx.cursor()

    # Get the details of the worst selling products from the database
    cursor.execute(f"SELECT A.`id`, A.`desc`, COALESCE(SUM(B.`qty`), 0) AS total_qty_sold "
                   f"FROM {STOCK_TABLE} A "
                   f"LEFT JOIN {SALES_TABLE} B on A.`id` = B.`id` "
                   "GROUP BY A.`id`, A.`desc` "
                   "ORDER BY total_qty_sold, A.`last_updated` "
                   "LIMIT 10")
    rows = cursor.fetchall()
    
    if (rows):
        display.table_header(("Product ID", 10), ("Description", 36), ("Qty Sold", 8))

        for row in rows:
            print(f"{row[0]: 10}", f"{row[1][:36]: <36}", row[2])
    else:
        print("\nNot Enough Data")

    # Close the cursor
    cursor.close()

def show(cnx):
    display.subheading("Show Analytics")
    print("\n1. Most Valuable Customers")
    most_valuable_customers(cnx)
    print("\n2. Stock Alert")
    stock_alert(cnx)
    print("\n3. Best Selling Products")
    best_selling_products(cnx)
    print("\n4. Worst Selling Products")
    worst_selling_products(cnx)
    input("\nPress any key to continue : ")
