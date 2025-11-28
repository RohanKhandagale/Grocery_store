from sql_connection import  get_sql_connection

def get_all_products(conn):
    cursor = conn.cursor()
    query = (
        "SELECT Products.product_id, Products.name, Products.uom_id, Products.price_per_unit, uom.uom_name "
        "FROM Products "
        "INNER JOIN uom ON Products.uom_id = uom.uom_id"
    )
    cursor.execute(query)

    response = []

    for product_id,name,uom_id,price_per_unit,uom_name in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id':uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )
    return response

def insert_new_product(conn, product):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Products (name, uom_id, price_per_unit) VALUES (?, ?, ?)",
        (product['name'], product['uom_id'], product['price_per_unit'])
    )
    conn.commit()

def delete_product(conn,product_id):
    cursor = conn.cursor()
    cursor.execute( "Delete From Products where product_id = ?",
        (product_id, )
    )
    conn.commit()
if __name__=='__main__':
    conn = get_sql_connection()
    print(delete_product(conn,8))

