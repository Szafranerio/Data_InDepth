class Bank():
    
    def __init__(self,name, amount = 0):
        self.name = name
        self.amount = amount
        
    def add_money(self,value):
        self.amount = self.amount + value 
        
    def withdraw(self, money=0):
        self.money = money
        if self.money>self.amount:
            print ('Not enough funds')
        else:
            self.amount=self.amount - self.money
            return f'New balance is {self.amount}'  

b = Bank('Bartek', 50)
print(b.amount)
b.add_money(100)
print(b.amount)
b.withdraw(10000)
print(b.amount)