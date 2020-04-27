'''
Created on Aug 5, 2015

@author: Deepak_M05
'''
from utility import DBConnectivity
from classes.ProductModule import Product

''' 
This function retrieves all the products belonging to a particular category
'''

def get_products(category):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_products=[]
        cur.execute("select productid, productname, price from sample_product where category=:category",{"category":category})
        for product_id,name,price in cur:
            '''
            In this loop, we are creating a product object for every row
            and setting the values from the row into the product object
            '''
            product=Product()
            product.set_price(price)
            product.get_price
            
         
                            
            product.set_product_id(product_id)
            product.set_product_name(name)
            
            '''
            Here were are adding the product to a list
            '''
            list_of_products.append(product)
            
        return list_of_products
        
    finally:
        cur.close()
        con.close()

    