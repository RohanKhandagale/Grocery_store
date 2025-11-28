Grocery App

This Python project is a Grocery Store Management Web Application designed as a 3-tier application.

🏗 Architecture (3-Tier)
1. Front End

HTML

CSS

JavaScript

Bootstrap

2. Backend

Python

Flask

3. Database

MSSQL

📌 Description

The Grocery App allows users to manage products, units of measure, and orders.
After initial deployment, user feedback was collected. The following exercises describe the enhancements and fixes required.

🧪 Exercises (User Feedback to Address)
Products Module

Add an Edit button for products

On the products page, add an Edit button next to the existing Delete button.

Editing should allow modifying existing product details.

Add new UOM (Unit of Measure)

Implement a new form to allow adding UOMs (e.g., Cubic Meter if the store starts selling wood).

Requires changes in both:

Backend (Python/Flask)

Frontend (UI)

Orders Module

Add form validation

Currently, orders can be placed without validation.

Add validation for:

Empty customer name

Invalid item name

Missing or invalid quantity

This is frontend-only work.

Fix total price not updating grand total

When users manually change the total price of an item, the grand total should update accordingly.

Fix this bug on the order creation page.

Add View button in orders list

In the orders grid, add a View button in the last column.

On click, it should display full order details including:

Items

Quantity

Price

Total
