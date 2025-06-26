

-- 1. Inner Join: address table and order table on customer ID
select ship_amount, ship_date, line1, city 
from my_guitar_shop.orders 
inner join my_guitar_shop.addresses 
on my_guitar_shop.orders.customer_id = my_guitar_shop.addresses.customer_id;

-- 2. Inner Join: customer and order table on customer id
select first_name, last_name, ship_amount, ship_date 
from my_guitar_shop.customers 
inner join my_guitar_shop.orders 
on my_guitar_shop.customers.customer_id = my_guitar_shop.orders.customer_id;

-- 3. Inner Join: customer and address table on customer id
select first_name,last_name, line1, city,state, zip_code  
from my_guitar_shop.customers 
inner join my_guitar_shop.addresses 
on my_guitar_shop.customers.customer_id = my_guitar_shop.addresses.customer_id;

-- 4. Inner Join: order_items and products table on product id
select product_name, list_price, order_id
from my_guitar_shop.products
inner join my_guitar_shop.order_items  
on my_guitar_shop.products.product_id = my_guitar_shop.order_items.product_id;

-- 5. Inner Join: orders and order_item table on order_id
select  first_name, last_name, product_name,ship_amount
from my_guitar_shop.customers c
inner join my_guitar_shop.orders o  
on c.customer_id = o.customer_id
inner join my_guitar_shop.order_items oi 
on o.order_id = oi.order_id
inner join my_guitar_shop.products p 
on oi.product_id = p.product_id;

-- 6. Group By:
select order_id, AVG(ship_amount) as average_amount
from my_guitar_shop.orders
group by order_id;

-- 7. Group By: 
select product_id, SUM(oi.item_price * oi.quantity) AS total_sales
from my_guitar_shop.order_items oi
group by oi.product_id
order by total_sales DESC;

-- 8. Group By:
select first_name, last_name, count(*) as customer_count
from my_guitar_shop.customers 
group by first_name, last_name;

-- 9. Group By:
select c.category_name, count(p.product_id) as product_count
from my_guitar_shop.categories c
join my_guitar_shop.products p
on c.category_id = p.category_id
group by c.category_name;

-- 10. Group By: 
select c.first_name, c.last_name, p.product_name, sum(o.ship_amount) as total_shipping
from my_guitar_shop.customers c
inner join my_guitar_shop.orders o
on c.customer_id = o.customer_id
inner join my_guitar_shop.order_items oi
on o.order_id = oi.order_id
inner join my_guitar_shop.products p
on oi.product_id = p.product_id
group by c.customer_id, p.product_id
order by total_shipping desc;

