# Start by creating a Store class that has 2 attributes: a name and a list of products. 
# The name must be provided upon creation, but the products list should be empty.

class Store:
    
    product_list = []
    
    def __init__(self,name,product):
        self.name = name
        self.product = product