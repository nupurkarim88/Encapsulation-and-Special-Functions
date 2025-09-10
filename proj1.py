#START
class MyCllass:
  __privateVar = 27

  def __privateMethod(self):
    print(" private method")

  def hello(self):
    print("Printing the private variable:", self.__privateVar)

m1 = MyCllass()
m1.hello()
#END