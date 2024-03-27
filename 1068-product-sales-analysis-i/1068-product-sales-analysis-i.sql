select product_name, year, price
FROM sales 
INNER JOIN Product
ON sales.product_id=Product.product_id