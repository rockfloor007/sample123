from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, atm_pin, username, balance):
        self.__atm_pin = atm_pin  # ENCAPSULATION
        self.username = username
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

class securedata(BankAccount):

    def withdraw(self,amount):
        if  amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn successfully"
        return "/insufficient funds"

    def deposit(self,amount):
        self.balance += amount
        return f"{amount} deposited successfully"

class premiumaccount(BankAccount):

    def withdraw(self,amount):
        if  amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn successfully"
        return "/insufficient funds"

    def deposit(self,amount):
        return "Premium deposit processed faster"

#sanjay = premiumaccount("123456","sanjay",1000)
sanjay = premiumaccount(atm_pin="123456", username="sanjay", balance=1000)
john = securedata(atm_pin="123456", username="sanjay", balance=1000)


print(john.withdraw(100))
print(sanjay.withdraw(100))
print(sanjay.deposit(100))