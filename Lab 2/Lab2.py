def show_menu():
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def atm_program():
    balance = 1000.0
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"You deposited ${amount:.2f}. New balance: ${balance:.2f}")
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"You withdrew $ {amount:.2f}. New balance: ${balance:.2f}")
            else:
                print("Insufficient funds.")
        elif choice == "4":
            print("Thank you for trusting this ATM. Bye!")
            break
        else:
            print("Invalid choice. Please try again.")

atm_program()