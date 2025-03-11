# mock_product_api.py

import random

def fetch_product_data(product_id):
    # Simulate fetching product data from a database or external service
    products_data = {
        101: {'name': 'Product A', 'price': 199.99, 'category': 'Electronics'},
        102: {'name': 'Product B', 'price': 149.99, 'category': 'Clothing'},
        103: {'name': 'Product C', 'price': 299.99, 'category': 'Home & Kitchen'},
        104: {'name': 'Product D', 'price': 99.99, 'category': 'Books'}
    }
    
    if product_id in products_data:
        return products_data[product_id]
    else:
        return None

# Example usage
product_id = 103
product_data = fetch_product_data(product_id)
if product_data:
    print(f"Product Data for Product {product_id}: {product_data}")
else:
    print(f"No data found for Product {product_id}")
