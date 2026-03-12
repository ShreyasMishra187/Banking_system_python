balance = 0

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    balance += amount
    print("Deposit successful!")
    print("Current balance:", balance)


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print("Current balance:", balance)


def check_balance():
    print("Your current balance is: ₹", balance)


while True:

    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        deposit()

    elif choice == "2":
        withdraw()

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("Thank you for using the banking system!")
        break

    else:
        print("Invalid option")