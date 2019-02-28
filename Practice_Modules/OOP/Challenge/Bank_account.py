class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def show_balance(self):
        balance = self.balance 
        print("Your balance is: ", balance)
    
    def deposit(self, amount):
        self.balance += amount
        print("deposit approved!")
        print("New balance is after deposit: ",self.balance)    


    def withdraw(self, amount):
        if(amount > self.balance):
            print("withdraw denied!")
            print("Cannot withdraw. Need more funds")

        if (amount < self.balance): 
            print("withdraw approved!")
            self.balance -= amount
            print("New balance is after withdrawal: ", self.balance)
    
    def __str__(self):
        return f"The owner is {self.owner} and the balance is {self.balance}"
        

    

#Instantiate the Account
a = Account("Me", 500)

#print the owner of the account
print(a.owner)

#print account balance without using a method
print(a.balance)

#show balance of account, should be 500
a.show_balance()

#deposit 500 into account
a.deposit(500)

#withdraw 1001 from the account, but since 1001 is more than the bank account balance, it wont withdraw money.
a.withdraw(1001)

#show the balance, should be 1000, because started off with 500, deposited 500, then tried to withdraw 1001, but did not.  So should still be 1000.
a.show_balance()

print(a)

