def show_balance(balance):
    print(f"Your current balance is: ${float(balance)}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return amount + balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    return balance - amount

def logout(name):
    print("Goodbye", name)