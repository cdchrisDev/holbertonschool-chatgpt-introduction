#!/usr/bin/python3
class Checkbook:
    """A func to registry
    user funds

    Properties:
        -- self.balance = 0.0

    Methods:
        -- Deposit(self, amount): set the deposit 
        amount according to user input

        -- withdraw(self, amount): set the withdraw 
        by user input

        -- get_balance: Show the actual balance
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """A func to set the deposit amount

        Properties:
            -- self.amount (int)

        Example:
            >>> Checkbook(5000)
            >>> Checkbook.deposit(9000)
            Deposited 9000
            Current Balance 18000
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """A func to withdraw by user input

        Example:
            >>> Checkbook(5000)
            >>> Checkbook.withdraw(500)
            Withdrew 500
            Current Balance 4500

            >>> Checkbook(10)
            >>> Checkbook.withdraw(11)
            Insufficient funds to complete the withdrawal.

        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """A func to show the actual balance"""

        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
            if action.lower() == 'exit':
                break
            elif action.lower() == 'deposit':
                amount = float(input("Enter the amount to deposit: $")) #No crash anymore
                cb.deposit(amount)
            elif action.lower() == 'withdraw':
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            elif action.lower() == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
        except:
            amount = 0.0

if __name__ == "__main__":
    main()
