class mohamed():
   def __init__(self,mname,price):
      self.mname=mname
      self.price=price
      print('My name is ')
   def name(self):
      print('your name is')
class Ahmed(mohamed):
   def __init__(self,mname,price,amount):
      super().__init__(mname,price)
      self.amount=amount
      print(f'my name is {self.mname} and price is {self.price} And amount {self.amount}')
   def moh(self,nom):
      self.nom=nom
      print(f'moh {self.nom}')
myname=Ahmed('mustafa',150,600)
myname.moh('k')