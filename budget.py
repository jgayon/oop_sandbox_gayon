import string
from typing_extensions import Self
from random import randint

class Budget:
 def __init__(self, category:str, initial_balance:float) -> None:
    self.category = category
    self.initial_balance = initial_balance
    self.running_balance = initial_balance
 
 def get_running_balance(self)-> float:
    return self.running_balance

 def withdraw(self,amount:float) -> None:
    self.running_balance = self.running_balance - amount
    

 def deposit(self,amount:float) -> None:
    self.running_balance = self.running_balance + amount

class User:
    def __init__(self, name: str, total_budget:float) -> None:
       self.name = name
       self.total_budget = total_budget
       self.id = randint(1,1000)
       budgets = {}
    
    def add_budget(self, category: str, initial_balance:float) -> None:
        budget = Budget(category=category,initial_balance=initial_balance)
        self.budgets.update({category: budget})
    
    def transfer_balance(self, sender:str, reciever:str, amount:float)-> None:
        pass

