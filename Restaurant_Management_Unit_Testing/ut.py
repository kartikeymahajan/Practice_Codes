from HTMLTestRunner import HTMLTestRunner
import unittest
from main import *

class Test(unittest.TestCase):

    def test_is_ordered_item_available(self):

        '''Checking is ordered item available in our menu card using assertIn()'''

        Restaurant.cursor.execute("SELECT * FROM menu_card")
        menu_card = Restaurant.cursor.fetchall()

        menu_card_items = [item[1].title() for item in menu_card]
        
        item = obj.item_name
        self.assertIn(item, menu_card_items)
        

    def test_is_item_quantity_int(self): 

        '''Checking the given quantity of item is integer using assertEqual()'''
        
        quantity = obj.quantity
        self.assertEqual(type(quantity), int)

    
    def test_order_quantity(self):

        '''Checking the order quantity, should be less than or equal to 10'''

        quantity = obj.quantity

        self.assertLessEqual(quantity, 10, "Quantity should be less than 10")

    
    def test_mobile_number_length(self): 

        '''Checking customers mobile number lenght, 10 numbers required.'''      

        Mobile_number = obj.mobile_number

        test = len(Mobile_number) == 10

        self.assertTrue(test, "Please check the length of mobile number, should be 10")


    def test_is_mobile_number_indian(self):

        '''Checking the number is valid indian number'''      

        Mobile_number = obj.mobile_number

        test = Mobile_number.startswith(("6","7","8","9"))

        self.assertTrue(test, "Please enter a valid indian mobile number")


if __name__ == '__main__':  
    # begin the 
    unittest.main() 
    # HTMLTestRunner.main()
