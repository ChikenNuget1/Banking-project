"""
Bank account manager
 - Create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount, and BusinessAccount.
   Manage credits and debits from these accounts through an ATM style program.

Todo
- Add more features
    Current version seems very lacking
- Add error-handling
"""

class Account:
    def __init__(self):
        self.checking = CheckingAccount()
        self.saving = SavingsAccount()
        self.business = BusinessAccount()
        self.current_acount = None
        self.acc_list = [self.checking, self.saving, self.business]
        self.main_screen()
    
    def main_screen(self):
        print("Current Accounts:\n1. Checking Account\n2. Savings Account\n3. Business Account\n4. Check balance of all accounts")
        user_input = int(input("Which account? "))
        print()
        match user_input:
            case 1: self.current_acount = self.checking
            case 2: self.current_acount = self.saving
            case 3: self.current_acount = self.business
            case 4: self.check_balance()
        
        print(self.current_acount)

        print("Select the process:\n1. Deposit\n2. Withdraw\n3. Exchange")
        user_input2= int(input("Which process? "))
        print()
        match user_input2:
            case 1: self.change_money()
            case 2: self.change_money()
            case 3: self.send_money()

    def send_money(self):
        ac_list = self.acc_list
        ac_list.remove(self.current_acount)
        for i in range(len(ac_list)):
            print(f"{i+1}. {ac_list[i]}")
        user_input = int(input("Which account should we send the money to? "))
        match user_input:
            case 1: send_to_acc = ac_list[0]
            case 2: send_to_acc = ac_list[1]
        money_to_send = 9999999
        while money_to_send > self.current_acount.get_balance():
            money_to_send = float(input("How much should we send? "))
        send_to_acc.change_money(money_to_send)
        self.current_acount.change_money(money_to_send*-1)
        print("\n")
        self.main_screen()

    def change_money(self):
        print(self.current_acount)
        print("Please enter a negative number to withdraw and a positive number to deposit")
        user_input = float(input("Please enter a number: "))
        print()
        self.current_acount.change_money(user_input)
        self.main_screen()

    def check_balance(self):
        print("Checking balance on all accounts...")
        for i in self.acc_list:
            print(i)
        print()
        self.main_screen()

class CheckingAccount:
    def __init__(self):
        self.money = 0

    def change_money(self, money_to_change):
        if isinstance(money_to_change, float):
            self.money += money_to_change
        if not isinstance(money_to_change, float):
            print("Please enter a valid number")
    
    def send_money(self, money_to_send):
        if isinstance(money_to_send, float) and money_to_send > 0:
            self.money -= money_to_send
        else:
            print("Please enter a valid number")

    def get_balance(self):
        return self.money

    def __str__(self):
        return f"Checking Account has ${self.money}"

class SavingsAccount:
    def __init__(self):
        self.money = 0

    def change_money(self, money_to_change):
        if isinstance(money_to_change, float):
            self.money += money_to_change
        if not isinstance(money_to_change, float):
            print("Please enter a valid number")

    def send_money(self, money_to_send):
        if isinstance(money_to_send, float) and money_to_send > 0:
            self.money -= money_to_send
        else:
            print("Please enter a valid number")

    def get_balance(self):
        return self.money

    def __str__(self):
        return f"Savings Account has ${self.money}"

class BusinessAccount:
    def __init__(self):
        self.money = 0

    def change_money(self, money_to_change):
        if isinstance(money_to_change, float):
            self.money += money_to_change
        if not isinstance(money_to_change, float):
            print("Please enter a valid number")

    def send_money(self, money_to_send):
        if isinstance(money_to_send, float) and money_to_send > 0:
            self.money -= money_to_send
        else:
            print("Please enter a valid number")

    def get_balance(self):
        return self.money

    def __str__(self):
        return f"Business Account has ${self.money}"
    
if __name__ == "__main__":
    Account()