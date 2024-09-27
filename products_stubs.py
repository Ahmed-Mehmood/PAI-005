class Product:
  def _init_(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
       if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
        
       if quantity < 10:
         unit_price = self.price  # Fixed: this line should have a proper assignment
       elif 10 <= quantity < 50:
        unit_price = self.price * 0.9
       else:  # This covers quantity >= 50
        unit_price = self.price * 0.8

        product_price = quantity * unit_price
        return product_price


  def make_purchase(self, quantity):
      pass

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase