from sys import stderr
from product import Product, Sold_Product
import customer
from bill import Bill
import stock
import display

STOCK_TABLE = "stock"
CUSTOMER_TABLE = "customers"
BILL_TABLE = "bills"
SALES_TABLE = "sales"
MIN_BILL_NO = 100001

def generate_bill_no(cnx) -> int:
    # Create cursor object
    cursor = cnx.cursor()

    # Fetch the last row from the table
    cursor.execute(f"SELECT `bill_no` from `{BILL_TABLE}` ORDER BY `bill_no` DESC LIMIT 1")
    row = cursor.fetchone()

    # Assign bill number to the new bill
    if row:
        bill_no = row[0] + 1
    else:
        bill_no = MIN_BILL_NO

    # Close the cursor
    cursor.close()

    return bill_no

def add_to_cart(cnx):
    # Search and select the product to be added to the cart
    results = stock.search_product(cnx, True)
    
    if sp := stock.select_product(results, "\nSelect the product to be added to the cart"):
        while True:
            try:
                req_qty = int(input("\nEnter quantity : "))

                if req_qty <= 0:
                    raise ValueError
            
            except ValueError:
                print("Invalid quantity. Please try again.", file = stderr)
                continue
            else:
                break
        
        p = Product(id = sp.get_id(), desc = sp.get_desc(), qty = req_qty,
                    MRP = sp.get_MRP(), price = sp.get_price(), GST = sp.get_GST())
        return p, sp.get_qty()
    else:
        return None
    
def get_customer_dues(cnx, mobile_no: int) -> float:
    # Create cursor object
    cursor = cnx.cursor()

    # Get customer dues
    cursor.execute(f"SELECT `dues` from `{CUSTOMER_TABLE}` "
                   f"WHERE `mobile_no` = {mobile_no}")
    row = cursor.fetchone()

    # Close the cursor
    cursor.close()

    return float(row[0])

def set_customer_dues(cnx, mobile_no: int, dues: float) -> None:
    # Create cursor object
    cursor = cnx.cursor()

    # Update the dues for the specified customer in the database
    cursor.execute(f"UPDATE `{CUSTOMER_TABLE}` "
                   f"SET `dues` = {dues} "
                   f"WHERE `mobile_no` = {mobile_no}")
    
    # Commit the changes to the database
    cnx.commit()

    # Close the cursor
    cursor.close()
    
def record_purchase(cnx, b: Bill) -> None:
    # Create cursor object
    cursor = cnx.cursor()

    for p in b.get_cart():
        # Update the entry of the stock table
        cursor.execute(f"UPDATE `{STOCK_TABLE}` "
                       f"SET `qty` = `qty` - {p.get_qty()} "
                       f"WHERE `id` = {p.get_id()}")

        # Create instance of class `Sold_Product`
        sp = Sold_Product(bill_no = b.get_bill_no(), timestamp = b.get_timestamp(),
                          id = p.get_id(), desc = p.get_desc(), qty = p.get_qty(),
                          MRP = p.get_MRP(), price = p.get_price(), GST = p.get_GST())
        
        # Insert entry into the sales table
        cursor.execute(f"INSERT INTO `{SALES_TABLE}` "
                       f"VALUES ({sp.get_id()}, '{sp.get_desc()}', {sp.get_qty()}, "
                       f"{sp.get_MRP()}, {sp.get_price()}, {sp.get_GST()}, "
                       f"{sp.get_bill_no()}, '{sp.get_timestamp()}')") 
        
    # Insert the bill entry into the database
    cursor.execute(f"INSERT INTO `{BILL_TABLE}` "
                   f"VALUES ({b.get_bill_no()}, {b.get_mobile_no()}, '{b.get_timestamp()}', "
                   f"{b.get_total_items()}, {b.get_total_qty()}, {b.get_total_amount()}, "
                   f"{b.get_net_amount()}, {b.get_amount_paid()})")
    
    # Commit changes to the database
    cnx.commit()

    # Close the cursor
    cursor.close()

    return set_customer_dues(cnx, b.get_mobile_no(), b.get_net_amount() - b.get_amount_paid())

def generate_bill(cnx) -> None:
    display.subheading("Generate Bill")

    # Search and select the customer
    c = customer.search(cnx)

    # Create instance of class `bill.Bill`
    b = Bill(generate_bill_no(cnx), c)

    while True:
        print("\nAdd Product(s) to Cart (1)")
        print("Remove Product from Cart (2)")
        print("List All Selected Product(s) (3)")
        print("Modify Customer Details (4)")
        print("Proceed to Checkout (0)")

        try:
            opt = int(input("\nSelect an Option : "))
        except ValueError:
            print("Invalid option. Please try again.", file = stderr)
        else:
            
            if opt in range(0, 5):
                if opt == 0:
                    dues = get_customer_dues(cnx, c.get_mobile_no())
                    b.checkout(dues)

                    if b.get_total_items():
                        # Print the generated bill
                        b.print()

                        # Print thanks message
                        print()
                        print("Thank you for shopping! :)".center(display.CONSOLE_WIDTH))

                        # Input the amount paid by the customer
                        amount_paid = 0

                        while True:
                            try:
                                amount_paid = float(input("\nEnter the amount paid by the customer : "))
                            except ValueError:
                                print("Invalid amount. Please try again.", file = stderr)
                                continue
                            else:
                                break

                        b.set_amount_paid(amount_paid)

                        # Record the purchase
                        record_purchase(cnx, b)
                    else:
                        print("Shopping Cart Empty. Bill Generation Aborted.", file = stderr)
                    
                    break
                elif opt == 1:
                    if t := add_to_cart(cnx):
                        if b.add_product(*t):
                            print("Product Added to the Cart")
                elif opt == 2:
                    b.remove_product()
                elif opt == 3:
                    b.list_products()
                elif opt == 4:
                    customer.modify(cnx, c)
            else:
                print("Invalid option. Please try again.", file = stderr)
