
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        
    # Let's give some methods to our Product class:
    #     update_price(self, percent_change, is_increased) - updates the product's price. 
    #     If is_increased is True, the price should increase by the percent_change provided. 
    #     If False, the price should decrease by the percent_change provided.
    #     print_info(self) - print the name of the product, its category, and its price.
    
    def update_price(self, percent_change,is_increased):
        self.percent_change = percent_change
        
        if is_increased == True:
            self.price += percent_change * self.price
        else:
            self.price -= percent_change * self.price
            
    # print_info(self) - print the name of the product, its category, and its price.
    def print_info(self):
        print(f'Product Name: {self.name} \nCategory: {self.category} \nPrice: ${self.price}')
        
product_1 = Product("Apple Watch Series 8",399.99,"Accessory")
product_1.print_info()