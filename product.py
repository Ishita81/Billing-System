from sys import stderr
from datetime import datetime

# Define the class `product``
class Product:
    def __init__(self, id: int, desc: str, qty: int, 
                 MRP: float, price: float, GST: int):

        # Primary key
        self._id = id

        self._desc = desc
        self._qty = qty
        self._MRP = MRP
        self._price = price
        self._GST = GST
    
    def get_id(self) -> int:
        return self._id

    def get_desc(self) -> str:
        return self._desc
        
    def get_qty(self) -> int:
        return self._qty
        
    def get_MRP(self) -> float:
        return self._MRP
        
    def get_price(self) -> float:
        return self._price
        
    def get_GST(self) -> int:
        return self._GST
    
    def set_qty(self, qty) -> None:
        self._qty = qty
    
    def print(self, style = "tabular"):
        if style == "tabular":
            print(f"{self._id: <10}", self._desc[:36].ljust(36), f"{self._qty: <6}", 
                  f"{self._MRP: <9}", f"{self._price: <9}", f"{self._GST: <5}")
        elif style == "stacked":
            print(f"\nProduct ID : {self._id}")
            print(f"Description : {self._desc}")
            print(f"Available Quantity : {self._qty}")
            print(f"MRP : Rs {self._MRP}")
            print(f"Price : Rs {self._price}")
            print(f"GST : {self._GST}")
    
# Derive the class `stock_product` from the class `product`
class Stock_Product(Product):
    def __init__(self, id: int, desc: str = '', qty: int = 0, 
                 MRP: float = 0, price: float = 0, GST: int = 0,
                 last_updated = datetime(1, 1, 1, 0, 0, 0), initial_qty = 0):
        
        super().__init__(id, desc, qty, MRP, price, GST)
        
        self.__last_updated = last_updated
        self.__initial_qty = initial_qty

    def get_last_updated(self) -> datetime:
        return self.__last_updated
    
    def get_initial_qty(self) -> int:
        return self.__initial_qty

    def add(self):
        while True:
            try:
                self._desc = input("\nEnter Product Description : ")
                self._qty = self.__initial_qty = int(input("Enter Quantity : "))
                self._MRP = float(input("Enter MRP : "))
                self._price = float(input("Enter Price : "))

                if not (self._qty > 0 and self._MRP > 0 and self._price > 0):
                    raise ValueError
                
                if self._price > self._MRP:
                    raise ValueError

                self._GST = int(input("Enter GST (as applicable on this product) : "))
                
                if not (self._GST >= 0 and self._GST <= 100):
                    raise ValueError

            except ValueError:
                print("\nInvalid value(s). Please try again.", file = stderr)
                continue
            else:
                break
            finally:
                self.__last_updated = datetime.now()
    
    def modify(self):
        element = input("\nChange (D)escription | (Q)uantity | (M)RP | (P)rice | (G)ST : ")
        
        while True:
            try:
                if element == 'd' or element == 'D':
                    self._desc = input("\nEnter New Product Description : ")
                elif element == 'q' or element == 'Q':
                    self._qty = int(input("\nEnter New Quantity : "))

                    if not (self._qty > 0):
                        raise ValueError

                    self.__last_updated = datetime.now()
                    self.__initial_qty = self._qty

                elif element == 'm' or element == 'M':
                    self._MRP = float(input("\nEnter New MRP : "))
                elif element == 'p' or element == 'P':
                    self._price = float(input("\nEnter New Price : "))
                elif element == 'g' or element == 'G':
                    self._GST = int(input("\nEnter New GST (as applicable on this product) : "))
                else:
                    print("Invalid Selection", file = stderr)
                    return False

                if not (self._MRP > 0 and self._price > 0):
                    raise ValueError
                
                if not (self._GST >= 0 and self._GST <= 100):
                    raise ValueError
                
            except ValueError:
                print("Invalid value. Please try again.", file = stderr)
                continue
            else:
                break

        return True

# Derive the class `sold_product` from the class `product`
class Sold_Product(Product):
    def __init__(self, bill_no: int, timestamp: datetime, id: int,
                 desc: str, qty: int, MRP: float, price: float = 0,
                 GST: int = 0):
        
        super().__init__(id, desc, qty, MRP, price, GST)
        self.__bill_no = bill_no
        self.__timestamp = timestamp

    def get_bill_no(self) -> int:
        return self.__bill_no
    
    def get_timestamp(self) -> datetime:
        return self.__timestamp
