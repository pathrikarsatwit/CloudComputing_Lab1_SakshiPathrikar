import mysql.connector
from tests import TestDatabase  

def driver():
    sqlQueries = {
        "1" : "select ship_amount, ship_date, line1, city from my_guitar_shop.orders inner join my_guitar_shop.addresses on my_guitar_shop.orders.customer_id = my_guitar_shop.addresses.customer_id",
        "2" : "select first_name, last_name, ship_amount, ship_date  from my_guitar_shop.customers inner join my_guitar_shop.orders on my_guitar_shop.customers.customer_id = my_guitar_shop.orders.customer_id",
        "3" : "select first_name,last_name, line1, city,state, zip_code from my_guitar_shop.customers inner join my_guitar_shop.addresses on my_guitar_shop.customers.customer_id = my_guitar_shop.addresses.customer_id",
        "4" : "select product_name, list_price, order_id from my_guitar_shop.products inner join my_guitar_shop.order_items on my_guitar_shop.products.product_id = my_guitar_shop.order_items.product_id",
        "5" : "select  first_name, last_name, product_name,ship_amount from my_guitar_shop.customers c inner join my_guitar_shop.orders o on c.customer_id = o.customer_id inner join my_guitar_shop.order_items oi on o.order_id = oi.order_id inner join my_guitar_shop.products p on oi.product_id = p.product_id",
        "6" : "select order_id, AVG(ship_amount) as average_amount from my_guitar_shop.orders group by order_id",
        "7" : "select product_id, SUM(oi.item_price * oi.quantity) AS total_sales from my_guitar_shop.order_items oi group by oi.product_id order by total_sales DESC",
        "8" : "select first_name, last_name, count(*) as customer_count from my_guitar_shop.customers group by first_name, last_name",
        "9" : "select c.category_name, count(p.product_id) as product_count from my_guitar_shop.categories c join my_guitar_shop.products p on c.category_id = p.category_id group by c.category_name",
        "10" : "select c.first_name, c.last_name, p.product_name, sum(o.ship_amount) as total_shipping from my_guitar_shop.customers c inner join my_guitar_shop.orders o on c.customer_id = o.customer_id inner join my_guitar_shop.order_items oi on o.order_id = oi.order_id inner join my_guitar_shop.products p on oi.product_id = p.product_id group by c.customer_id, p.product_id order by total_shipping desc"        
    }
    continueLoop = True
    while (continueLoop): 
        for key, value in sqlQueries.items():
            print(key, value)
            print("\n")
        userinput = input("Enter the sql query number you want to execute, enter 0 to exit or enter 11 to run tests: ")
        
        if userinput == "0":
            print("Byee :)")
            continueLoop = False
        elif userinput=="11":
            print("Tests: ")
            TestDatabase()
        else :
            print("userinput sql queries: \n", sqlQueries.get(userinput))
            mydb = connect_to_db()
            query_addresses(mydb, sqlQueries[userinput])
            


def connect_to_db():
    try:

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="Sakshi@1234",
            database="my_guitar_shop"
        )
        print("Successfully connected to MySQL database!")
        print(f"Connected using port: {mydb._port}")
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")

    return mydb


def query_addresses(mydb, query):
    try:
        
        # Establish a connection to the MySQL database
        if mydb == None:
            print("reconnection to db required")
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="my_guitar_shop"
            )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Define the SQL SELECT query
        sql_query = query

        # Execute the query
        mycursor.execute(sql_query)

        # Fetch all the results
        # Use fetchone() to retrieve a single row, or fetchmany(size) for a specific number of rows
        results = mycursor.fetchall()

        # Iterate through the fetched results and print them
        for row in results:
            print("\n" , row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and the database connection
        if mydb.is_connected():
            mydb.close()
        print("MySQL connection closed.")

if __name__ == "__main__":
    driver()
    