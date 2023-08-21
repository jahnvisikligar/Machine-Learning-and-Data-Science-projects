# Data-Science-Challenge

## Part 1: Working with Python

Given some sample data, write a program to answer the following: click here to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

What metric would you report for this dataset?

What is its value?

## Part 2: Working with SQL

a.  How many orders were shipped by Speedy Express in total?

    SELECT *

    FROM Orders

    LEFT JOIN Shippers

    ON Orders.ShipperID = Shippers.ShipperID

    WHERE ShipperName = "Speedy Express"


b.	What is the last name of the employee with the most orders?

    SELECT Employees.LastName, Count(Orders.OrderID) As NumberOfOrders From Orders

    INNER Join Employees ON Orders.EmployeeID = Employees.EmployeeID

    Group by LastName Order by NumberOfOrders ASC

    Limit 10;


c.	What product was ordered the most by customers in Germany?

    SELECT p.ProductName, SUM(Quantity) AS TotalQuantity

    FROM Orders AS o, OrderDetails AS od, Customers AS c, Products AS p

    WHERE c.Country = "Germany" AND od.OrderID = o.OrderID AND od.ProductID = p.ProductID AND c.CustomerID = o.CustomerID

    GROUP BY p.ProductID

    ORDER BY TotalQuantity DESC

    LIMIT 10;


