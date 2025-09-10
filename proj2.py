class Computer:
  def __init__(self):
    self.__maxprice = 900

  def sell(self):
    print(f"Selling price: {self.__maxprice}")

  def setMaxPrice(self, price):
    self.__maxprice = price


c = Computer()
c.sell()
c.setMaxPrice(1000)
c.sell()