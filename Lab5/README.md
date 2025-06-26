# CloudComputing_Lab5_SakshiPathrikar

1. Introduction To your project
    1. This project demonstrates 5 Inner Joins and 5 Group By Queries

2. Description of your project
    1. The project consists of a set of SQL queries executed on the my_guitar_shop database, which includes tables such as:
        1. addresses
        2. administrators
        3. categories
        4. customers
        5. orders
        6. order_items
        7. products

3. Design of your project
    1. The project contains queries that: 
        1. Retrieves shipping information and address information
        2. Gets customer names and their shipping data
        3. Gets customers names and address details
        4. Gets product name, product price and which order number is the product associated with
        5. Gets first name, last name of the customer, the product they have purchased and the number of times they have purchased this product
        6. Gets the average number of times an order has been shipped
        7. Calculates the total sales (the price of the item * number of times it has been ordered) and arranges it in descending order.
        8. Groups the unique customers together
        9. Groups the same products from each category and gets their count
        10. Groups the customers, orders, order items, and products to show which customers bought which products and how many times. 

4. Detailed instructions on how to run your project
    1. Download Lab5_Scripts.sql
    2. In DBeaver: 
        1. Start up DBeaver, download and load the my_guitar_shop database
        2. Then from File>Open FIle open the downladed script (Lab5_Scripts.sql)
        3. To run all queries at once, select the scroll icon with the run button (Execute SQL Script)
        4. To run a query individually or only a certain number of queries, select the query/queries and click the play button (Execute SQL Query)