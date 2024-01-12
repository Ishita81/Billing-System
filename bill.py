from sys import stderr
from datetime import datetime
from typing import List
from product import Product
from customer import Customer
import display

# Define the exception `QtyUnavailable`
class QtyUnavailableError(Exception):
    '''
    Insufficient quantity
    '''
    pass

class Bill:
    __GSTIN: str = "29ABCDE1234F1Z5"
    __phone_no: str = "+91 XXXXX XXXXX"

    def __init__(self, bill_no: int, customer: Customer):
        self.__bill_no = bill_no
        self.__customer = customer
        self.__timestamp = datetime(1, 1, 1, 0, 0, 0)
        self.__cart: List[Product] = []
        self.__total_items: int = 0
        self.__total_qty: int = 0
        self.__total_amount: float = 0
        self.__net_amount: float = 0
        self.__amount_paid: float = 0

    def get_bill_no(self) -> int:
        return self.__bill_no
    
    def get_mobile_no(self) -> int:
        return self.__customer.get_mobile_no()
    
    def get_timestamp(self) -> datetime:
        return self.__timestamp
    
    def get_cart(self) -> List[Product]:
        return self.__cart
    
    def get_total_items(self) -> int:
        return self.__total_items
    
    def get_total_qty(self) -> int:
        return self.__total_qty
    
    def get_total_amount(self) -> float:
        return self.__total_amount
    
    def get_net_amount(self) -> float:
        return self.__net_amount
    
    def get_amount_paid(self) -> float:
        return self.__amount_paid
    
    def set_amount_paid(self, amount_paid: float):
        self.__amount_paid = amount_paid
    
    def add_product(self, p: Product, s_qty: int) -> bool:
        # Search if the cart already contains this product
        index = None

        for i, cp in enumerate(self.__cart):
            if cp.get_id() == p.get_id():
                index = i
                break

        # Add product to the cart
        try:
            if index is not None:
                cp = self.__cart[index]
            
                # Check if the stock quantity is greater than or equal to the cart quantity
                if (s_qty >= cp.get_qty() + p.get_qty()):
                    cp.set_qty(cp.get_qty() + p.get_qty())
                else:
                    raise QtyUnavailableError
            else:
                # Check if the requested quantity is less tahn or equal to the stock quantity 
                if p.get_qty() <= s_qty:
                    self.__cart.append(p)
                else:
                    raise QtyUnavailableError
        except QtyUnavailableError:
            print("The requested quantity is unavailable. Please check back later.", file = stderr)
            print(f"Available Quantity : {s_qty}")
            return False

        return True

    def remove_product(self):
        if self.__cart:
            to_remove = input("\nEnter Product ID or Description : ")

            if to_remove.isdigit():
                to_remove = int(to_remove)
        
            # Search for the product in the cart
            index = None

            for i, p in enumerate(self.__cart):
                if isinstance(to_remove, int):
                    if to_remove == p.get_id():
                        index = i
                        break
                else:
                    if to_remove.lower() in p.get_desc().lower():
                        index = i
                        break

            if index is not None:
                # Print product details
                self.__cart[index].print(style = "stacked")

                # Remove product from the cart
                self.__cart.pop(index)
                print("\nProduct Removed from the Cart")
            else:
                #Print error message
                print("No products matching the specified criteria were found.", file = stderr)
        else:
            print("\nCart is Empty")

    def list_products(self, string = "\nCart Summary : "):
        print(string)

        # List all the products in the cart
        if self.__cart:
            # Display table header
            display.table_header(("Product ID", 10), ("Description", 36), ("Qty", 6),
                                 ("MRP", 9), ("Price", 9), ("GST", 5))

            for p in self.__cart:
                p.print()
        else:
            print("Cart is Empty")

    def checkout(self, dues: float = 0):
        # Set timestamp
        self.__timestamp = datetime.now()

        # Calculate total items, total quantity, and the total amount to be paid
        self.__total_items = len(self.__cart)
        self.__total_amount = self.__net_amount = dues

        for p in self.__cart:
            self.__total_qty += p.get_qty()
            self.__total_amount += (p.get_qty() * p.get_MRP())
            self.__net_amount += (p.get_qty() * (p.get_price() * ((100 + p.get_GST()) / 100)))
        
        # Round off the total amount to two decimal places
        self.__net_amount = round(self.__net_amount, 2)

    def print(self):
        print()
        display.heading()
        print()
        print(f"GSTIN: {self.__GSTIN}".ljust(display.CONSOLE_WIDTH // 2), end = '')
        print(f"Phone No.: {self.__phone_no}")
        print(f"Bill No. : {self.__bill_no}".ljust(display.CONSOLE_WIDTH // 2), end = '')
        print(f"Date and Time : {self.__timestamp.strftime('%Y/%m/%d %H:%M:%S')}")

        # Print customer details
        print("\nCustomer Details :")
        self.__customer.print()
        
        # List all the products in the cart
        self.list_products("\nShopping Summary : ")

        print(f"\nTotal Items : {self.__total_items}".ljust(display.CONSOLE_WIDTH // 2), end = '')
        print(f"Total Quantity : {self.__total_qty}")
        print(f"\nTotal Amount : Rs {self.__total_amount: .2f}")
        print(f"You Save : Rs {(self.__total_amount - self.__net_amount): .2f}")
        print(f"Net Amount to be Paid : Rs {self.__net_amount: .2f}")
