class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        print(f"Current balance: {self.balance}")

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


    while True:
        print("\nBANKING SYSTEM:")
        print("1. Create an account")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Check Balance")
        print("5. Display Account Info")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == 1:
            name = input("Enter your name: ")
            account_number = input("Enter your account number: ")

            account = BankAccount(account_number, name)
            print("Account created successfully.")


        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)


        elif choice == 3:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)


        elif choice == 4:
            account.get_balance()


        elif choice == 5:
            account.display_info()


        elif choice == 6:
            print("Exiting the program.")
        