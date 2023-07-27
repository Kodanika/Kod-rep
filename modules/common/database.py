import sqlite3 

class Database():
    
    def __init__(self):
        self.connection = sqlite3.connect(r'C:\\Users\\HP\\Kod-rep' + r'\\become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f'Connected successfully. SQLite Database Version is: {record}')
    
    def get_all_user(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_products_qnt_by_id(self, products_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {products_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE ID = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
             VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailes_orders(self):
        query = "SELECT orders.id, customers.name, products.name, products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def order_by_products_name(self):
        query = f"SELECT name FROM products ORDER BY name"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
       
    def get_all_data_from_table(self, table):
        query = f"SELECT * FROM '{table}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_sum_quantity_of_products(self):
        query = "SELECT SUM(quantity) FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def count_total_number_of_customers(self):
        query = "SELECT COUNT(id) FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_all_customers_and_orders(self):
        query = "SELECT customers.id, customers.name, customers.city, orders.order_date \
                FROM customers \
                LEFT JOIN orders ON customers.id = orders.customer_id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_product_whith_minimum_qnt_of_products(self):
        query = "SELECT name, description, quantity FROM products \
                GROUP BY name \
                HAVING MIN(quantity) <= 10"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
        
        
        



    

