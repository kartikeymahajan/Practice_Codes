import mysql.connector as c
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

class Restaurant:

    # Connection to Database
    con = c.connect(host = "localhost", user="root", passwd="admin", database="restaurant")
    cursor = con.cursor()

    # Here we are delcaring some variables to store data
    orders_list = []
    Customer_name = ""
    mobile_number = ""
    order_id = ""
    item_name = ""
    time_date = ""
    quantity = 0
    order_total = 0
    flag = True
    veg_nonveg = ""

    def __init__(self):
        print("\n*************** Wellcome to our Restaurant ***************\n")

        
    def take_customer_details(self):

        '''This funtion will take the details from customer'''

        self.Customer_name = input("Enter your name: ").title()
        self.mobile_number = input("Enter your mobile number: ")

        print("\nThank you..\n")

        # self.veg_nonveg = input("What do you want to order? Veg / Nonveg: ").lower

    def menu_card(self):

        '''In this funtion we are printing our menu_card from Database in well formate'''

        print("****************** This is our Menu Card ******************\n")

        # menu_card = pd.read_excel('menu_card.xlsx') # Fetching menu card using pandas

        engine = create_engine('mysql+mysqlconnector://root:admin@localhost/restaurant')
        query = "SELECT * FROM menu_card"
        menu_card = pd.read_sql_query(query, engine)
        print(menu_card)


    current_datetime = datetime.now()

    def take_order(self, food_menu):

        '''In this funtion we are taking the order details from user only if the item is available in menu card'''

        self.item_name = input("\nPlease type item name: ").title() 

        # Fetching the menu_card items from database
        self.cursor.execute(f"SELECT * FROM {food_menu}")
        menu_card = self.cursor.fetchall()
        menu_card_items = [item[1].title() for item in menu_card]

        if self.item_name in menu_card_items:
            self.quantity = int(input(f"Quanity of {self.item_name}: "))
            self.order_id = f"ORID{self.mobile_number[:5]}"
        else:
            print("\nSorry, this item is not available\n")
            self.flag = False

        if self.flag:
            # query to get item price from database
            self.cursor.execute(f"SELECT Rate FROM {food_menu} WHERE Item = '{self.item_name}'")
            rate = self.cursor.fetchone()
            self.order_total += (rate[0] * self.quantity)

            # query to store order_details in database
            self.time_date = self.current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            query = f"INSERT INTO order_details(order_id, item_name, quantity, time_date) VALUES('{self.order_id}','{self.item_name}',{self.quantity}, '{self.time_date}')"
            self.cursor.execute(query)
            self.con.commit()
            self.orders_list.append((self.item_name, self.quantity, (rate[0] * self.quantity)))

    def show_order_details(self):

        '''Funtion to show order details in proper bill formate'''

        print("*********Order Details*********\n\n")
        print(f"Order ID: {self.order_id}\n")
        print(f"Order Time: {self.time_date}\n")

        # Define column headers
        headers = ["Item", "Quantity", "Price"]

        # Print column headers
        print("{:<10} {:<10} {:<10}".format(*headers))

        for row in self.orders_list:
            print("{:<10} {:<10} {:<10}".format(row[0], row[1], row[2]))

        print(f"\nOrder Total: {self.order_total}\n")

class NonVeg(Restaurant):

    def __init__(self):
        super().__init__()

    def take_customer_details(self):
        super().take_customer_details()

    def menu_card(self):
        '''In this funtion we are printing our menu_card from Database in well formate'''

        print("****************** This is our Menu Card ******************\n")

        # menu_card = pd.read_excel('menu_card.xlsx') # Fetching menu card using pandas

        engine = create_engine('mysql+mysqlconnector://root:admin@localhost/restaurant')
        query = "SELECT * FROM non_veg_menu"
        menu_card = pd.read_sql_query(query, engine)
        print(menu_card)

    current_datetime = datetime.now()
    def take_order(self, food_menu):
        return super().take_order(food_menu)
    
    def show_order_details(self):
        return super().show_order_details()



'''************ Main program ************'''

# obj = Restaurant()
obj = Restaurant()

obj.take_customer_details()
obj.menu_card()

input1 = input("\nDo you want to order something? Y/N : ")

if input1 == "n" or input1 == "N":
     print("\nThanks for Visit, Come again.\n")

elif input1 == "y" or input1 == "Y":
    while True:
        if obj.flag:
            obj.take_order("menu_card")
            input2 = input("Do you want anything else? Y/N: ")
        if input2 in ["Y","y"]:
            obj.flag = True
            continue
        elif input2 in ["N","n"]:
            break
    
    if obj.flag:
        # Inserting customer data into database with order details
        query = f"insert into customer_details(name, number, order_id) values('{obj.Customer_name}','{obj.mobile_number}','{obj.order_id}')"
        obj.cursor.execute(query)
        obj.con.commit()

        # print(obj.orders_list)
        print("\nThank You, Your Order placed\n\n")
        obj.show_order_details()
    
    else:
        # Inserting customer data into database without order details
        query = f"insert into customer_details(name, number) values('{obj.Customer_name}','{obj.mobile_number}')"
        obj.cursor.execute(query)
        obj.con.commit()
        print("\nThank You, Please Come again.\n")
    
