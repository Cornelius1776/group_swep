import random

accounts_database = {}

# Open account
def create_account():
    name = input("Enter Your Full Name: ").strip()
    
    # Generating account number
    account_number = "24" + "".join(str(random.randint(0, 9)) for _ in range(8))
    
    # Set up a PIN
    while True:
        pin = input("Set a 4-digit PIN for your account: ").strip()
        if pin.isdigit() and len(pin) == 4:
            break
        print("Invalid PIN. Please enter exactly 4 digits.")
    
    # Store the account
    accounts_database[account_number] = {"name": name, "balance": 0.0, "pin": pin}
    
    print("\nAccount successfully created!")
    print(f"Account Number: {account_number}")
    print(f"Account Name: {name}\n")

# Verify user pin before transactions
def verify_pin(account_number):
    for _ in range(3):  # Allow 3 attempts
        entered_pin = input("Enter your 4-digit PIN: ").strip()
        if accounts_database[account_number]["pin"] == entered_pin:
            return True
        print("Incorrect PIN. Try again.")
    print("Too many incorrect attempts.")
    return False

# Deposit
def deposit(account_number):
    if verify_pin(account_number):
        try:
            amount = float(input("Enter amount to deposit in Naira: "))
            if amount > 0:
                accounts_database[account_number]["balance"] += amount
                print(f"Successfully deposited: ₦{amount:.2f}")
                print(f"New balance: ₦{accounts_database[account_number]['balance']:.2f}")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Withdrawal
def withdraw(account_number):
    if verify_pin(account_number):
        try:
            amount = float(input("Enter amount to withdraw in Naira: "))
            if 0 < amount <= accounts_database[account_number]["balance"]:
                accounts_database[account_number]["balance"] -= amount
                print(f"Successfully withdrawn: ₦{amount:.2f}")
                print(f"New balance: ₦{accounts_database[account_number]['balance']:.2f}")
            else:
                print("Invalid amount. Ensure you have sufficient funds and enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Check balance
def check_balance(account_number):
    if verify_pin(account_number):
        balance = accounts_database[account_number]["balance"]
        print(f"Your Current Balance is: ₦{balance:.2f}")

# Using the program
def open_program():
    # program loop.
    while True:
        print("\n--- Welcome To Group Five Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            create_account()
        elif choice in {"2", "3", "4"}:
            account_number = input("Enter your account number: ").strip()
            if account_number in accounts_database:
                if choice == "2":
                    deposit(account_number)
                elif choice == "3":
                    withdraw(account_number)
                elif choice == "4":
                    check_balance(account_number)
            else:
                print("Account number not found.")
        elif choice == "5":
            print("Exiting the banking system. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")


open_program()
