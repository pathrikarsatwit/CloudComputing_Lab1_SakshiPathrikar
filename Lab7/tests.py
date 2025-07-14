import mysql.connector

class TestDatabase():
    def __init__(self):
        self.test_connection()
        self.test_query1()
        self.test_query2()
        self.test_query3()
        self.test_query4()
        self.test_query5()
        self.test_query6()
        self.test_query7()
        self.test_query8()
        self.test_query9()
        self.test_query10()

    def test_connection(self):
        try:
            self.mydb = mysql.connector.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="Sakshi@1234",
                database="my_guitar_shop"
            )
            print("Successfully connected to MySQL database!")
            print(f"Connected using port: {self.mydb._port}")
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            self.mydb = None

    def connect_db(self, query):
        try:
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(query)
            results = self.mycursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print(f"Failure connecting to database: {err}")
            return None

    def test_query1(self):
        query = "select ship_amount, ship_date, line1, city from my_guitar_shop.orders inner join my_guitar_shop.addresses on my_guitar_shop.orders.customer_id = my_guitar_shop.addresses.customer_id"
        rows = self.connect_db(query)
        if rows and "Paramus" in rows[0]:
            print("Success executing Query 1")
        else:
            print("Failed executing query 1")

    def test_query2(self):
        query = "select first_name, last_name, ship_amount, ship_date from my_guitar_shop.customers inner join my_guitar_shop.orders on my_guitar_shop.customers.customer_id = my_guitar_shop.orders.customer_id"
        rows = self.connect_db(query)
        if rows and "Zimmer" in rows[1]:
            print("Success executing Query 2")
        else:
            print("Failed executing query 2")

    def test_query3(self):
        query = "select first_name,last_name,line1,city,state,zip_code from my_guitar_shop.customers inner join my_guitar_shop.addresses on my_guitar_shop.customers.customer_id = my_guitar_shop.addresses.customer_id"
        rows = self.connect_db(query)
        if rows and len(rows[0]) == 6:
            print("Success executing Query 3")
        else:
            print("Failed executing query 3")

    def test_query4(self):
        query = "select product_name,list_price,order_id from my_guitar_shop.products inner join my_guitar_shop.order_items on my_guitar_shop.products.product_id = my_guitar_shop.order_items.product_id"
        rows = self.connect_db(query)
        if rows and len(rows[0]) == 3:
            print("Success executing Query 4")
        else:
            print("Failed executing query 4")

    def test_query5(self):
        query = "select first_name,last_name,product_name,ship_amount from my_guitar_shop.customers c inner join my_guitar_shop.orders o on c.customer_id = o.customer_id inner join my_guitar_shop.order_items oi on o.order_id = oi.order_id inner join my_guitar_shop.products p on oi.product_id = p.product_id"
        rows = self.connect_db(query)
        if rows:
            print("Success executing Query 5")
        else:
            print("Failed executing query 5")

    def test_query6(self):
        query = "select order_id, AVG(ship_amount) as average_amount from my_guitar_shop.orders group by order_id"
        rows = self.connect_db(query)
        if rows and len(rows[0]) == 2:
            print("Success executing Query 6")
        else:
            print("Failed executing query 6")

    def test_query7(self):
        query = "select product_id, SUM(oi.item_price * oi.quantity) AS total_sales from my_guitar_shop.order_items oi group by oi.product_id order by total_sales DESC"
        rows = self.connect_db(query)
        if rows and len(rows[0]) == 2:
            print("Success executing Query 7")
        else:
            print("Failed executing query 7")

    def test_query8(self):
        query = "select first_name, last_name, count(*) as customer_count from my_guitar_shop.customers group by first_name, last_name"
        rows = self.connect_db(query)
        if rows and len(rows[0]) == 3:
            print("Success executing Query 8")
        else:
            print("Failed executing query 8")

    def test_query9(self):
        query = "select c.category_name, count(p.product_id) as product_count from my_guitar_shop.categories c join my_guitar_shop.products p on c.category_id = p.category_id group by c.category_name"
        rows = self.connect_db(query)
        if rows:
            print("Success executing Query 9")
        else:
            print("Failed executing query 9")

    def test_query10(self):
        query = "select c.first_name, c.last_name, p.product_name, sum(o.ship_amount) as total_shipping from my_guitar_shop.customers c inner join my_guitar_shop.orders o on c.customer_id = o.customer_id inner join my_guitar_shop.order_items oi on o.order_id = oi.order_id inner join my_guitar_shop.products p on oi.product_id = p.product_id group by c.first_name, c.last_name, p.product_name"
        rows = self.connect_db(query)
        if rows:
            print("Success executing Query 10")
        else:
            print("Failed executing query 10")

if __name__ == "__main__":
    TestDatabase()
