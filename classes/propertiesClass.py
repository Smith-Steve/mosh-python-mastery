class Product:
    def __init__(self, price=1):
        self.price = price
    
    @property
    #When python sees this, it will automatically create a property called, 'price'.
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

product = Product(-10)
print(product.price)