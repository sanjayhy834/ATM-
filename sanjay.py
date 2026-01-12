ICIC_Teja = {"Name": "Teja",
            "Moblie": "12345566",
            "ATM PIN" :"1234",
            "Balance" : 4567,
            "Transaction History" : []}     # this is the user data
print("Please insert your ATM card")
remaining_attempts  3
while reamining_attempts > 0 :
    user_pin = input("Enter your 4 digit pin: ")
    if len(user_pin) == 4:
        if user_pin in ICIC_Teja['ATM PIN'] :
            print("Welcom to ICIC ATM")
            user_input = int(input("Enter \n1.deposite money \n2.Withdraw money \n3.Check balance \n4.Change pin \n5.Transaction Histroy"))
            if user_input == 1:
                Deposite_money = int(input("Enter amount you want to deposite into the account: "))
                if Deposite_money >= 1000 and Deposite_money % 100 == 0:
                    ICIC_Teja['Balance'] += Deposite_money
                    ICIC_Teja['Tranction History'].append(f"Deposited: {Deposite_money}")
                    break
                elif user_input == 2:
                    Withdraw_money = int(input("Enter amount you want to withdraw from the amount: "))
                    if Withdraw_money <= ICIC_Teja['Balance'] and Withdraw_money % 100 == 0:
                        ICIC_Teja['Balance'] -= Withdraw_money
                        ICIC_Teja['Transaction History'].append(Withdraw_money)
                        print(f"You have withdraw {Withdraw_money} and the total balance in your account is {ICIC_Teja['Balance']}")
                        break
                    else:
                        print(f"your total balance is {ICIC_Teja['ATM PIN']} and you're trying to withdraw {Withdraw_money}'")
                elif user_input ==3:
                    print(f'Your total balance is {ICIC_Teja['Balance']}')
                    break
        else:
            remaining_attempts == 1
            if remaining_attempts > 0 :
                print(f"invalied pin entered and you have {reamining_attempts}")
            else:
                print("You've run out of attempts, your card has been temporarily blocked")
                break
    else:
        print("Please enter 4 digit pin only")