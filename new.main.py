print("Welcome to the Bank ATM") 
Trials = 3  
balance = 1000  

userpin = int(input("Set a 4-digit PIN for your account: "))
print("Your PIN has been set successfully!\n")

while Trials != 0:
    try:
        pin = int(input("Please Enter Your PIN Number: ")) 
        if pin != userpin:
            Trials -= 1
            print(f"Wrong PIN Number. {Trials} Trials Left.")
        else:
            while True:
                print("\nOptions:")
                print("1: Check Balance")
                print("2: Deposit Money")
                print("3: Withdraw Money")
                print("4: Exit")
                
                userChoice = input("Please select an option (1/2/3/4): ")
                
                if userChoice == "1":
                    print(f"Your current balance is {balance} £.")
                
                elif userChoice == "2":
                    try:
                        userDeposit = float(input("Enter the deposit amount: "))
                        if userDeposit > 0:
                            balance += userDeposit
                            print(f"{userDeposit} £ has been deposited into your account.")
                        else:
                            print("Invalid deposit amount. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                
                elif userChoice == "3":
                    try:
                        userWithdraw = float(input("Enter the amount to withdraw: "))
                        if 0 < userWithdraw <= balance:
                            balance -= userWithdraw
                            print(f"{userWithdraw} £ has been withdrawn from your account.")
                        elif userWithdraw > balance:
                            print("Insufficient balance. Please try again.")
                        else:
                            print("Invalid withdrawal amount. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                
                elif userChoice == "4":
                    print("Thank you for using Bank ATM. Goodbye!")
                    exit()
                
                else:
                    print("Invalid option. Please select a valid option (1/2/3/4).")
    
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    
print("You have been locked out of the system. Please contact your bank.")
