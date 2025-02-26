
class Bank_account():
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance
        
    def deposit(self,amount):
        self.__balance += amount
        print(f'Deposit {amount} after Deposit amount {self.__balance} ')

    def check_balance(self):
        return self.__balance
    
bal = Bank_account('123565765',15000)
bal.deposit(2000)
_balance = bal.check_balance()

print(_balance)
