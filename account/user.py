import re

#changed 

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self): 
        total = 0
        for account in self.accounts:
            total += account.get_balance()
        return total

    def get_account_count(self):
        account_count = len(self.accounts)
        return account_count

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return "Account removed successfully"
        return "Account not found"

    def is_valid_email(self, email):
        # Basic email validation using regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: ${self.get_total_balance()}"