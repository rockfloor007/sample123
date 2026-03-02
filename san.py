class securedata(BankAccount):

    def withdraw(self,amount):
        if  amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn successfully"
        return "/insufficient funds"

    def deposit(self,amount):
        self.balance += amount
        return f"{amount} deposited successfully"