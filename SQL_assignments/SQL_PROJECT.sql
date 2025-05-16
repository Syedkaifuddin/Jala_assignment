-- Create and use database
CREATE DATABASE IF NOT EXISTS happy_ai;
USE happy_ai;

-- Create SALESPEOPLE table
CREATE TABLE SALESPEOPLE (
    SNUM INT PRIMARY KEY,
    SNAME VARCHAR(50),
    CITY VARCHAR(50),
    COMM DECIMAL(4,2)
);

-- Create CUST table
CREATE TABLE CUST (
    CNUM INT PRIMARY KEY,
    CNAME VARCHAR(50),
    CITY VARCHAR(50),
    RATING INT,
    SNUM INT,
    FOREIGN KEY (SNUM) REFERENCES SALESPEOPLE(SNUM)
);

-- Create ORDERS table
CREATE TABLE ORDERS (
    ONUM INT PRIMARY KEY,
    AMT DECIMAL(10,2),
    ODATE DATE,
    CNUM INT,
    SNUM INT
    -- Note: Foreign keys skipped for CNUM because 2008 is not in CUST
);

-- Insert data into SALESPEOPLE
INSERT INTO SALESPEOPLE (SNUM, SNAME, CITY, COMM) VALUES
(1001, 'Peel', 'London', 0.12),
(1002, 'Serres', 'San Jose', 0.13),
(1004, 'Motika', 'London', 0.11),
(1007, 'Rafkin', 'Barcelona', 0.15),
(1003, 'Axelrod', 'New york', 0.10);

-- Insert data into CUST
INSERT INTO CUST (CNUM, CNAME, CITY, RATING, SNUM) VALUES
(2001, 'Hoffman', 'London', 100, 1001),
(2002, 'Giovanne', 'Rome', 200, 1003),
(2003, 'Liu', 'San Jose', 300, 1002),
(2004, 'Grass', 'Brelin', 100, 1002),
(2006, 'Clemens', 'London', 300, 1007),
(2007, 'Pereira', 'Rome', 100, 1004);

-- Insert data into ORDERS (2008 is unknown, so no FK constraint here)
INSERT INTO ORDERS (ONUM, AMT, ODATE, CNUM, SNUM) VALUES
(3001, 18.69, '1994-10-03', 2008, 1007),
(3003, 767.19, '1994-10-03', 2001, 1001),
(3002, 1900.10, '1994-10-03', 2007, 1004),
(3005, 5160.45, '1994-10-03', 2003, 1002),
(3006, 1098.16, '1994-10-04', 2008, 1007),
(3009, 1713.23, '1994-10-04', 2002, 1003),
(3007, 75.75, '1994-10-05', 2004, 1002),
(3008, 4723.00, '1994-10-05', 2006, 1001),
(3010, 1309.95, '1994-10-06', 2004, 1002),
(3011, 9891.88, '1994-10-06', 2006, 1001);


--                QUERIES                       
-- 1.	Display snum,sname,city and comm of all salespeople.

SELECT SNUM,SNAME, CITY, COMM FROM SALESPEOPLE;

-- OR

SELECT * FROM salespeople;


-- 2.	Display all snum without duplicates from all orders.

SELECT DISTINCT SNUM FROM ORDERS;

-- 3.	Display names and commissions of all salespeople in london.

SELECT SNAME, COMM FROM SALESPEOPLE
WHERE CITY = 'LONDON';

-- 4.	All customers with rating of 100.

SELECT * FROM CUST
WHERE RATING = 100;

-- 5.	Produce orderno, amount and date form all rows in the order table.

SELECT ONUM, AMT, ODATE  FROM ORDERS;

-- 6.	All customers in San Jose, who have rating more than 200.

SELECT * FROM CUST
WHERE CITY = "SAN JOSE" AND RATING > 200;

-- 7.	All customers who were either located in San Jose or had a rating above 200.

SELECT * FROM CUST
WHERE CITY = "SAN JOSE" OR RATING > 200;


-- 8.	All orders for more than $1000.

SELECT * FROM ORDERS 
WHERE AMT > 1000;

-- 9.	Names and citires of all salespeople in london with commission above 0.10.

SELECT SNAME, CITY FROM SALESPEOPLE
WHERE CITY = "LONDON" AND COMM > 0.10;

-- 10.	All customers excluding those with rating <= 100 unless they are located in Rome.

SELECT * FROM CUST
WHERE NOT (RATING <= 100 AND CITY != 'Rome');
 
-- 11.	All salespeople either in Barcelona or in london.

SELECT * FROM SALESPEOPLE 
WHERE CITY IN ('Barcelona', 'London');

-- 12.	All salespeople with commission between 0.10 and 0.12. (Boundary values should be excluded)

SELECT * FROM salespeople 
WHERE comm > 0.10 AND comm < 0.12;

-- 13.	All customers with NULL values in city column.

SELECT * FROM cust WHERE city IS NULL;

-- 14.	All orders taken on Oct 3Rd   and Oct 4th  1994.

SELECT * FROM orders 
 WHERE odate IN ('1994-10-03', '1994-10-04');

-- 15.	All customers serviced by peel or Motika.

SELECT * FROM cust 
WHERE snum IN (
    SELECT snum FROM salespeople WHERE sname IN ('Peel', 'Motika')
);

-- 16.	All customers whose names begin with a letter from A to B.

SELECT * FROM cust
 WHERE cname LIKE 'A%' OR cname LIKE 'B%';

-- 17.	All orders except those with 0 or NULL value in amt field.

SELECT * FROM orders 
WHERE amt IS NOT NULL or amt = 0;

-- 18.	Count the number of salespeople currently listing orders in the order table.

SELECT COUNT(DISTINCT snum) 
FROM orders;

-- 19.	Largest order taken by each salesperson, datewise.

SELECT snum, odate, MAX(amt) AS max_amt
FROM orders
GROUP BY snum, odate;

-- 20.	Largest order taken by each salesperson with order value more than $3000.

SELECT snum, MAX(amt) AS max_amt
FROM orders
WHERE amt > 3000
GROUP BY snum;

-- 21.	Which day had the hightest total amount ordered.

SELECT odate, SUM(amt) AS total_amt
FROM orders
GROUP BY odate
ORDER BY total_amt DESC
LIMIT 1;


-- 22.	Count all orders for Oct 3rd.

SELECT COUNT(*) FROM orders 
WHERE odate = '1994-10-03';

-- 23.	Count the number of different non NULL city values in customers table.

SELECT COUNT(DISTINCT city) FROM cust 
WHERE city IS NOT NULL;

-- 24.	Select each customer’s smallest order.

SELECT cnum, MIN(amt) AS smallest_order
FROM orders
GROUP BY cnum;

-- 25.	First customer in alphabetical order whose name begins with G.

SELECT * FROM cust 
WHERE cname LIKE 'G%' 
ORDER BY cname ASC 
LIMIT 1;

-- 26.	Get the output like “ For dd/mm/yy there are ___ orders.

SELECT DATE_FORMAT(odate, '%d/%m/%y') AS date, COUNT(*) AS order_count
FROM orders
GROUP BY odate
LIMIT 200;

-- 27.	Assume that each salesperson has a 12% commission. Produce order no., salesperson no., and amount of salesperson’s commission for that order.

SELECT onum, snum, amt * 0.12 AS commission 
FROM orders;

-- 28.	Find highest rating in each city. Put the output in this form. For the city (city), the highest rating is : (rating).

SELECT 
  CONCAT('For the city ', city, ', the highest rating is: ', MAX(rating)) AS result
FROM cust
GROUP BY city;

-- 29.	Display the totals of orders for each day and place the results in descending order.

SELECT odate, SUM(amt) AS total_amt
FROM orders
GROUP BY odate
ORDER BY total_amt DESC;

-- 30.	All combinations of salespeople and customers who shared a city. (ie same city).

SELECT s.sname, c.cname, s.city
FROM salespeople s
JOIN cust c ON s.city = c.city;

-- 31.	Name of all customers matched with the salespeople serving them.

SELECT c.cname, s.sname
FROM cust c
JOIN salespeople s ON c.snum = s.snum;

-- 32.	List each order number followed by the name of the customer who made the order.

SELECT o.onum, c.cname
FROM orders o
JOIN cust c ON o.cnum = c.cnum;

-- 33.	Names of salesperson and customer for each order after the order number.

SELECT o.onum, s.sname, c.cname
FROM orders o
JOIN salespeople s ON o.snum = s.snum
JOIN cust c ON o.cnum = c.cnum;

-- 34.	Produce all customer serviced by salespeople with a commission above 12%.

SELECT c.*
FROM cust c
JOIN salespeople s ON c.snum = s.snum
WHERE s.comm > 0.12;

-- 35.	Calculate the amount of the salesperson’s commission on each order with a rating above 100.

SELECT o.onum, o.amt * s.comm AS commission
FROM orders o
JOIN cust c ON o.cnum = c.cnum
JOIN salespeople s ON o.snum = s.snum
WHERE c.rating > 100;

-- 36.	Find all pairs of customers having the same rating.

SELECT c1.cnum AS customer1, c2.cnum AS customer2, c1.rating
FROM cust c1
JOIN cust c2 ON c1.rating = c2.rating ;

-- 37.	Find all pairs of customers having the same rating, each pair coming once only.

SELECT c1.cnum AS customer1, c2.cnum AS customer2, c1.rating
FROM cust c1
JOIN cust c2 ON c1.rating = c2.rating AND c1.cnum < c2.cnum;


-- 38.	Policy is to assign three salesperson to each customers. Display all such combinations.

SELECT c.cnum, c.cname, s.snum, s.sname
FROM cust c
JOIN (SELECT * FROM salespeople LIMIT 3) s;

-- 39.	Display all customers located in cities where salesman serres has customer.

SELECT *
FROM cust
WHERE city IN (
  SELECT city FROM cust WHERE snum = 1002
);

-- 40.	Find all pairs of customers served by single salesperson.

SELECT c1.cnum AS customer1, c2.cnum AS customer2, c1.snum
FROM cust c1
JOIN cust c2 ON c1.snum = c2.snum AND c1.cnum < c2.cnum;

-- 41.	Produce all pairs of salespeople which are living in the same city. Exclude combinations of salespeople with themselves as well as duplicates with the order reversed.

SELECT s1.snum AS salesperson1, s2.snum AS salesperson2, s1.city
FROM salespeople s1
JOIN salespeople s2 ON s1.city = s2.city AND s1.snum < s2.snum;

-- 42.	Produce all pairs of orders by given customer, names that customers and eliminates duplicates.

SELECT o1.onum AS order1, o2.onum AS order2, c.cname
FROM orders o1
JOIN orders o2 ON o1.cnum = o2.cnum AND o1.onum < o2.onum
JOIN cust c ON o1.cnum = c.cnum;

-- 43.	Produce names and cities of all customers with the same rating as Hoffman.

SELECT cname, city
FROM cust
WHERE rating = (SELECT rating FROM cust WHERE cname = 'Hoffman');

-- 44.	Extract all the orders of Motika.

SELECT *
FROM orders
WHERE snum = (SELECT snum FROM salespeople WHERE sname = 'Motika');

-- 45.	All orders credited to the same salesperson who services Hoffman.

SELECT *
FROM orders
WHERE snum = (SELECT snum FROM cust WHERE cname = 'Hoffman');

-- 46.	All orders that are greater than the average for Oct 4.

SELECT *
FROM orders
WHERE odate = '1994-10-04'
  AND amt > (
    SELECT AVG(amt) FROM orders WHERE odate = '1994-10-04'
  );

-- 47.	Find average commission of salespeople in london.

SELECT AVG(comm) AS avg_commission
FROM salespeople
WHERE city = 'London';

-- 48.	Find all orders attributed to salespeople servicing customers in london.

SELECT *
FROM orders
WHERE snum IN (
  SELECT DISTINCT snum FROM cust WHERE city = 'London'
);

-- 49.	Extract commissions of all salespeople servicing customers in London.

SELECT DISTINCT s.snum, s.comm
FROM salespeople s
JOIN cust c ON s.snum = c.snum
WHERE c.city = 'London';

-- 50.	Find all customers whose cnum is 1000 above the snum of serres.

SELECT *
FROM cust
WHERE cnum = (
  SELECT 1000 + snum FROM salespeople WHERE sname = 'Serres'
);

-- 51.	Count the customers with rating  above San Jose’s average.

SELECT COUNT(*)
FROM cust
WHERE rating > (
  SELECT AVG(rating) FROM cust WHERE city = 'San Jose'
);

-- 52.	Obtain all orders for the customer named Cisnerous. (Assume you don’t know his customer no. (cnum)).

SELECT *
FROM orders
WHERE cnum = (
  SELECT cnum FROM cust WHERE cname = 'Cisnerous'
);

-- 53.	Produce the names and rating of all customers who have above average orders.

SELECT DISTINCT c.cname, c.rating
FROM cust c
JOIN orders o ON c.cnum = o.cnum
GROUP BY c.cnum, c.cname, c.rating
HAVING AVG(o.amt) > (
  SELECT AVG(amt) FROM orders
);

-- 54.	Find total amount in orders for each salesperson for whom this total is greater than the amount of the largest order in the table.

SELECT snum, SUM(amt) AS total
FROM orders
GROUP BY snum
HAVING total > (
  SELECT MAX(amt) FROM orders
);

-- 55.	Find all customers with order on 3rd Oct.

SELECT DISTINCT c.*
FROM cust c
JOIN orders o ON c.cnum = o.cnum
WHERE o.odate = '1994-10-03';

-- 56.	Find names and numbers of all salesperson who have more than one customer.

SELECT snum, COUNT(*) AS customer_count
FROM cust
GROUP BY snum
HAVING COUNT(*) > 1;

-- 57.	Check if the correct salesperson was credited with each sale.

SELECT *
FROM orders o
WHERE NOT EXISTS (
  SELECT 1 FROM cust c WHERE o.cnum = c.cnum AND o.snum = c.snum
);

-- 58.	Find all orders with above average amounts for their customers.

SELECT *
FROM orders o
WHERE amt > (
  SELECT AVG(amt) FROM orders o2 WHERE o2.cnum = o.cnum
);

-- 59.	Find the sums of the amounts from order table grouped by date, eliminating all those dates where the sum was not at least 2000 above the maximum amount.

SELECT odate, SUM(amt) AS total
FROM orders
GROUP BY odate
HAVING total >= (
  SELECT MAX(amt) + 2000 FROM orders
);

-- 60.	Find names and numbers of all customers with ratings equal to the maximum for their city.

SELECT *
FROM cust c1
WHERE rating = (
  SELECT MAX(rating) FROM cust c2 WHERE c1.city = c2.city
);

-- 61.	Find all salespeople who have customers in their cities who they don’t service. ( Both way using Join and Correlated subquery.)

SELECT DISTINCT s.snum, s.sname, s.city
FROM salespeople s
JOIN cust c ON s.city = c.city
WHERE s.snum != c.snum;


-- 62.	Extract cnum,cname and city from customer table if and only if one or more of the customers in the table are located in San Jose.

SELECT cnum, cname, city
FROM cust
WHERE EXISTS (
    SELECT 1
    FROM cust
    WHERE city = 'San Jose'
);


-- 63.	Find salespeople no. who have multiple customers.

SELECT snum
FROM cust
GROUP BY snum
HAVING COUNT(*) > 1;


-- 64.	Find salespeople number, name and city who have multiple customers.

SELECT s.snum, s.sname, s.city
FROM salespeople s
JOIN cust c ON s.snum = c.snum
GROUP BY s.snum, s.sname, s.city
HAVING COUNT(c.cnum) > 1;

-- 65.	Find salespeople who serve only one customer.

SELECT s.snum, s.sname, s.city
FROM salespeople s
JOIN cust c ON s.snum = c.snum
GROUP BY s.snum, s.sname, s.city
HAVING COUNT(c.cnum) = 1;

-- 66.	Extract rows of all salespeople with more than one current order.

SELECT s.*
FROM salespeople s
JOIN orders o ON s.snum = o.snum
GROUP BY s.snum
HAVING COUNT(o.onum) > 1;

-- 67.	Find all salespeople who have customers with a rating of 300. (use EXISTS)

SELECT *
FROM salespeople s
WHERE EXISTS (
    SELECT 1
    FROM cust c
    WHERE c.snum = s.snum AND c.rating = 300
);

-- 68.	Find all salespeople who have customers with a rating of 300. (use Join).

SELECT DISTINCT s.*
FROM salespeople s
JOIN cust c ON s.snum = c.snum
WHERE c.rating = 300;

-- 69.	Select all salespeople with customers located in their cities who are not assigned to them. (use EXISTS).

SELECT s.*
FROM salespeople s
WHERE EXISTS (
    SELECT 1
    FROM cust c
    WHERE s.city = c.city AND s.snum != c.snum
);

-- 70.	Extract from customers table every customer assigned the a salesperson who currently has at least one other customer ( besides the customer being selected) with orders in order table.

SELECT c1.*
FROM cust c1
WHERE EXISTS (
    SELECT 1
    FROM cust c2
    JOIN orders o ON c2.cnum = o.cnum
    WHERE c1.snum = c2.snum AND c1.cnum != c2.cnum
);

-- 71.	Find salespeople with customers located in their cities ( using both ANY and IN).

SELECT *
FROM salespeople s
WHERE s.city = ANY (
    SELECT city FROM cust WHERE cust.snum = s.snum
);

-- using IN 

SELECT *
FROM salespeople s
WHERE s.city IN (
    SELECT city FROM cust WHERE cust.snum = s.snum
);

-- 72.	Find all salespeople for whom there are customers that follow them in alphabetical order. (Using ANY and EXISTS)

-- using any

SELECT *
FROM salespeople s
WHERE s.sname < ANY (
    SELECT cname FROM cust
);

-- using exists 

SELECT *
FROM salespeople s
WHERE EXISTS (
    SELECT 1
    FROM cust c
    WHERE c.cname > s.sname
);

-- 73.	Select customers who have a greater rating than any customer in rome.

SELECT *
FROM cust
WHERE rating > ANY (
    SELECT rating FROM cust WHERE city = 'Rome'
);

-- 74.	Select all orders that had amounts that were greater that atleast one of the orders from Oct 6th.

SELECT *
FROM orders
WHERE amt > ANY (
    SELECT amt FROM orders WHERE odate = '1994-10-06'
);

-- 75.	Find all orders with amounts smaller than any amount for a customer in San Jose. (Both using ANY and without ANY)

-- using any

SELECT *
FROM orders
WHERE amt < ANY (
    SELECT o.amt
    FROM orders o
    JOIN cust c ON o.cnum = c.cnum
    WHERE c.city = 'San Jose'
);

-- without using any

SELECT *
FROM orders
WHERE amt < (
    SELECT MIN(o.amt)
    FROM orders o
    JOIN cust c ON o.cnum = c.cnum
    WHERE c.city = 'San Jose'
);

-- 76.	Select those customers whose ratings are higher than every customer in Paris. ( Using both ALL and NOT EXISTS).

-- Using ALL
SELECT *
FROM cust
WHERE rating > ALL (
    SELECT rating FROM cust WHERE city = 'Paris'
);

-- Using NOT EXISTS

SELECT *
FROM cust c1
WHERE NOT EXISTS (
    SELECT 1
    FROM cust c2
    WHERE c2.city = 'Paris' AND c1.rating <= c2.rating
);

-- 77.	Select all customers whose ratings are equal to or greater than ANY of the Seeres.

SELECT *
FROM cust
WHERE rating >= ANY (
    SELECT rating
    FROM cust
    WHERE snum = (SELECT snum FROM salespeople WHERE sname = 'Seeres')
);

-- 78.	Find all salespeople who have no customers located in their city. ( Both using ANY and ALL)

-- Using ALL:

SELECT *
FROM salespeople s
WHERE city != ALL (
    SELECT city FROM cust WHERE cust.snum = s.snum
);

-- Using NOT EXISTS (alternative):


SELECT *
FROM salespeople s
WHERE NOT EXISTS (
    SELECT 1 FROM cust c
    WHERE c.city = s.city AND c.snum = s.snum
);

-- 79.	Find all orders for amounts greater than any for the customers in London.

SELECT *
FROM orders
WHERE amt > ANY (
    SELECT amt
    FROM orders o
    JOIN cust c ON o.cnum = c.cnum
    WHERE c.city = 'London'
);

-- 80.	Find all salespeople and customers located in london.

SELECT 'Salesperson' AS type, sname AS name, city
FROM salespeople
WHERE city = 'London'
UNION
SELECT 'Customer', cname, city
FROM cust
WHERE city = 'London';

-- 81.	For every salesperson, dates on which highest and lowest orders were brought.

-- Highest orders:
SELECT snum, odate, amt AS order_amt, 'Highest' AS type
FROM orders
WHERE (snum, amt) IN (
    SELECT snum, MAX(amt)
    FROM orders
    GROUP BY snum
)
UNION
-- Lowest orders:
SELECT snum, odate, amt, 'Lowest'
FROM orders
WHERE (snum, amt) IN (
    SELECT snum, MIN(amt)
    FROM orders
    GROUP BY snum
);

-- 82.	List all of the salespeople and indicate those who don’t have customers in their cities as well as those who do have.

SELECT s.snum, s.sname, s.city,
       CASE 
           WHEN EXISTS (
               SELECT 1 FROM cust c
               WHERE c.city = s.city AND c.snum = s.snum
           ) THEN 'Has customer in city'
           ELSE 'No customer in city'
       END AS status
FROM salespeople s;

-- 83.	Append strings to the selected fields, indicating weather or not a given salesperson was matched to a customer in his city.

SELECT s.snum, s.sname, s.city,
       CONCAT(s.sname, ' - ',
              CASE 
                  WHEN EXISTS (
                      SELECT 1 FROM cust c 
                      WHERE c.city = s.city AND c.snum = s.snum
                  ) THEN 'Matched'
                  ELSE 'Not Matched'
              END) AS result
FROM salespeople s;

-- 84.	Create a union of two queries that shows the names, cities and ratings of all customers. Those with a rating of 200 or greater will also have the words ‘High Rating’, while the others will have the words ‘Low Rating’.

SELECT cname, city, rating, 'High Rating' AS label
FROM cust
WHERE rating >= 200
UNION
SELECT cname, city, rating, 'Low Rating'
FROM cust
WHERE rating < 200;

-- 85.	Write command that produces the name and number of each salesperson and each customer with more than one current order. Put the result in alphabetical order.

SELECT s.sname AS name, s.snum AS num, 'Salesperson' AS type
FROM salespeople s
WHERE s.snum IN (
    SELECT snum
    FROM orders
    GROUP BY snum
    HAVING COUNT(*) > 1
)
UNION
SELECT c.cname, c.cnum, 'Customer'
FROM cust c
WHERE c.cnum IN (
    SELECT cnum
    FROM orders
    GROUP BY cnum
    HAVING COUNT(*) > 1
)
ORDER BY name;

-- 86.	Form a union of three queries. Have the first select the snums of all salespeople in San Jose, then second the cnums of all customers in San Jose and the third the onums of all orders on Oct. 3. Retain duplicates between the last two queries, but eliminates and redundancies between either of them and the first.

-- Salespeople in San Jose
SELECT snum AS id, 'Salesperson' AS type
FROM salespeople
WHERE city = 'San Jose'

UNION

-- Customers in San Jose
SELECT cnum, 'Customer'
FROM cust
WHERE city = 'San Jose'

UNION ALL

-- Orders on Oct 3 (retain duplicates)
SELECT onum, 'Order'
FROM orders
WHERE odate = '1994-10-03';  

-- 87.	Produce all the salesperson in London who had at least one customer there.

SELECT DISTINCT s.*
FROM salespeople s
JOIN cust c ON s.snum = c.snum
WHERE s.city = 'London' AND c.city = 'London';

-- 88.	Produce all the salesperson in London who did not have customers there.

SELECT *
FROM salespeople s
WHERE s.city = 'London' AND NOT EXISTS (
    SELECT 1 FROM cust c
    WHERE c.city = 'London' AND c.snum = s.snum
);

-- 89.	We want to see salespeople matched to their customers without excluding those salesperson who were not currently assigned to any customers. (User OUTER join and UNION)

SELECT s.sname AS salesperson, c.cname AS customer
FROM salespeople s
LEFT JOIN cust c ON s.snum = c.snum

UNION

SELECT s.sname, c.cname
FROM cust c
RIGHT JOIN salespeople s ON c.snum = s.snum;

