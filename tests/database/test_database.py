import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_user()
    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_products_qnt_update():
    db = Database()
    db.update_products_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові дані', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailes_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1
    
    # Check the data structure
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

@pytest.mark.database
def test_order_by_products_name():
    db = Database()
    orders_name = db.order_by_products_name()
    
    assert orders_name[0][0] == 'молоко'
   
@pytest.mark.database
def test_check_data_type_of_orders_table():
    db = Database()
    data = db.get_all_data_from_table('orders')
    
    assert type(data[0][0]) == int
    assert type(data[0][1]) == int
    assert type(data[0][2]) == int
    assert type(data[0][3]) == str

@pytest.mark.database
def test_check_data_type_of_customers_table():
    db = Database()
    data = db.get_all_data_from_table('customers')

    assert type(data[0][0]) == int
    assert type(data[0][1]) == str
    assert type(data[0][2]) == str
    assert type(data[0][3]) == str
    assert type(data[0][4]) == str

@pytest.mark.database
def test_check_total_sum_of_products():
    db = Database()
    total_sum = db.get_sum_quantity_of_products()

    assert total_sum[0][0] == 75

@pytest.mark.database
def test_check_count_of_customers():
    db = Database()
    total_number = db.count_total_number_of_customers()

    assert total_number[0][0] == 2

@pytest.mark.database
def test_products_qnt_cannot_be_updated():
    db = Database()
    try:
        db.update_products_qnt_by_id(2, 'молоко')
        milk_qnt = db.select_product_qnt_by_id(2)
        print ("Milk_quantity: ", milk_qnt)
    except:
        print('test_products_qnt_cannot_be_updated: OperationalError')

@pytest.mark.database
def test_product_cannot_be_inserted():
    db = Database()
    try:
        db.insert_product(5, 'морозиво', 'ванільне')
        ice_cream = db.select_product_qnt_by_id(5)
        print("Ice-cream_quantity:", ice_cream)
    except:
        print('test_product_cannot_be_inserted: TypeError')

@pytest.mark.database
def test_check_all_customers_and_orders():
    db = Database()
    customers_oders = db.get_all_customers_and_orders()
    print("All customers and oders: ", customers_oders)
    # Check quantity of customers equal to 2
    assert len(customers_oders) == 2
    # Check the data structure
    assert customers_oders[0][0] == 1
    assert customers_oders[0][1] == 'Sergii'
    assert customers_oders[0][2] == 'Kyiv'
    assert customers_oders[0][3] == '12:22:23'
    assert customers_oders[1][0] == 2
    assert customers_oders[1][1] == 'Stepan'
    assert customers_oders[1][2] == 'Kyiv'
    assert customers_oders[1][3] == None

@pytest.mark.database
def test_check_products_with_min_qnt():
    db = Database()
    min_qnt = db.get_product_whith_minimum_qnt_of_products()
    print(min_qnt)

    assert len(min_qnt) == 2
