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
    if quantity <= 0:
        print("Purchase quantity must be greater than zero.")
        return  # Added return to exit the function early

    if quantity > self.amount:
        print(f"Insufficient quantity: only {self.amount} items available.")
        return  # Added return to exit the function early

    total_price = self.get_price(quantity)
    self.amount -= quantity  # This is more concise
    print(f"Purchase successful: {quantity} {self.name}(s) bought for ${total_price:.2f}.")
    print(f"Remaining stock: {self.amount}")

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase