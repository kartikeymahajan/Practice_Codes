import pytest
from main import *


@pytest.fixture
def menu_card():
    Restaurant.cursor.execute("SELECT * FROM menu_card")
    menu_card_ = Restaurant.cursor.fetchall()

    menu_card_items = [item[1].title() for item in menu_card_]

    return menu_card_items

def test_is_ordered_item_available(menu_card):
    
    '''Checking is ordered item available in our menu card'''

    item_name = obj.item_name
    assert item_name in menu_card


def test_is_item_quantity_int():

    '''Checking the given quantity of item is integer'''

    quantity = obj.quantity
    assert type(quantity) == int


def test_order_quantity():

    '''Checking the order quantity, should be less than or equal to 10'''

    quantity = obj.quantity
    assert quantity <= 10


def test_mobile_number_length(): 

    '''Checking the length of customers mobile number, Should be 10.'''      

    Mobile_number = obj.mobile_number
    assert len(Mobile_number) == 10 


def test_is_mobile_number_indian():

    '''Checking the number is valid indian number'''      

    Mobile_number = obj.mobile_number
    assert Mobile_number.startswith(("6","7","8","9"))

