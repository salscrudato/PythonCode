
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def sayHello(self):
     return 'Hello my name is ' + self.name
 
  @staticmethod
  def staticSayHi():
      print('Hello Static Method')