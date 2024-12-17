print("Welcome to the Bank ATM")
Trials = 3
userpin= 1234

while Trials !=0:
    pin = int(input("Please Enter Your Ping Number: "))
    if pin != userpin:
        Trials -= 1
        print("Wrong pin Number", Trials, "Trials Left")
    else:
        userChoice = input("d: Deposit or w:Withdraw: ")
        if userChoice == "d":
            userDeposit = input("Enter The Deposit Amount: ")
            print(userDeposit, "£ Hvae been Deposited Into Your Account")
        if userChoice == "w":
            userWithdraw = input("Enter The Amout You Would Like To Withdraw: ")
            print(userWithdraw, "£ Have Been Withdraw From Your Account")
    userexit = input("would You Like To Continue? Y/N ")
    if userexit == "N":
        print("Thank you For Using Bank ATM")
        break
    else:
        continue