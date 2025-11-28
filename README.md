🛒 Grocery App

A Python-based Grocery Store Management Web Application built as a 3-tier application using:

Frontend: HTML, CSS, JavaScript, Bootstrap

Backend: Python, Flask

Database: MySQL

📘 Project Description

The Grocery App provides basic product and order management features. After giving the app to users, the following feedback was received. Your task is to implement the enhancements listed below.

🧪 Exercise Requirements
🔧 Products Module
✅ 1. Add Edit Button

On the products page that lists all products, add an Edit button next to the existing Delete button to allow editing product details.

✅ 2. Add New UOM (Unit of Measure)

Create a new form that allows adding additional Units of Measure.
Example: Adding Cubic Meter when the store decides to sell wood.

This requires modifying:

Frontend (UI form)

Backend (Python server routes)

🛒 Orders Module
✅ 3. Add Form Validation

Currently, an order can be placed without any validation.
You must add validation for:

Empty customer name

Invalid item name

Missing or invalid quantity

🔹 This is frontend-only work.

🐞 4. Fix Total Price – Grand Total Bug

On the new order page, changing the total price of an item manually does not update the grand total.
You need to fix this issue.

👁 5. Add “View” Button in Orders Grid

In the orders listing page, add a View button in the last column.
When clicked, it should show the order details including:

Items in the order

Item price

Quantity

Total price
