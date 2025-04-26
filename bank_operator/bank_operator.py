from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

#changed

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
        return
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if not users:
        print("No users available.")
        return
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    if not users:
        print("No users available. Create a user first.")
        return
    list_users()
    try:
        idx = int(input("Select user number: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection!")
            return
        
        print("Account Type:")
        print("1. Savings Account")
        print("2. Students Account")
        print("3. Current Account")
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))
        
        user = users[idx]
        
        if account_choice == 1:
            account = SavingsAccount(user.name, user.email, amount)
        elif account_choice == 2:
            account = StudentAccount(user.name, user.email, amount)
        elif account_choice == 3:
            account = CurrentAccount(user.name, user.email, amount)
        else:
            print("Invalid choice!")
            account = BankAccount(user.name, user.email, amount)

        users[idx].add_account(account)
        print(f"{account.get_account_type()} added!\n")
    except ValueError:
        print("Please enter valid numbers.")

def deposit_money():
    if not users:
        print("No users available.")
        return
    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection!")
            return
            
        user = users[idx]
        if not user.accounts:
            print("User has no accounts. Create an account first.")
            return
            
        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
            
        acc_idx = int(input("Select account: ")) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid account selection!")
            return
            
        amount = float(input("Enter amount to deposit: "))
        user.accounts[acc_idx].deposit(amount)
        print(f"Deposited Rs. {amount} successfully. New balance: Rs. {user.accounts[acc_idx].get_balance()}")
    except ValueError:
        print("Please enter valid numbers.")

def withdraw_money():
    if not users:
        print("No users available.")
        return
    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection!")
            return
            
        user = users[idx]
        if not user.accounts:
            print("User has no accounts. Create an account first.")
            return
            
        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
            
        acc_idx = int(input("Select account: ")) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid account selection!")
            return
            
        amount = float(input("Enter amount to withdraw: "))
        user.accounts[acc_idx].withdraw(amount)
        print(f"Current balance: Rs. {user.accounts[acc_idx].get_balance()}")
    except ValueError:
        print("Please enter valid numbers.")

def view_transactions():
    if not users:
        print("No users available.")
        return
    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection!")
            return
            
        user = users[idx]
        if not user.accounts:
            print("User has no accounts.")
            return
            
        for i, acc in enumerate(user.accounts):
            print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
            transactions = acc.get_transaction_history()
            if not transactions:
                print("No transactions yet.")
            else:
                for tx in transactions:
                    print(tx)
    except ValueError:
        print("Please enter valid numbers.")