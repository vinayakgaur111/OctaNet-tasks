import time

print("Please insert Your Card")

time.sleep(5)

password = 1234

pin = int(input("enter your atm pin "))

balance = 5000
if pin == password:
    while True:
        print("""
            1 == balaance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
        """)
        try:
            option = int(input("Please enter your choise "))
        except:
            print("Please enter valid option")
        if option == 1:
            print(f"Your current balance is {balance}")
            print("======================================")
        if option == 2:
            withdraw_amount = int(input("Please enter withdraw_amount "))
            print("======================================")
            print("======================================")
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debit from your account")
            print("======================================")
            print("======================================")
            print(f"your current balance is {balance}")
        if option == 3:
            deposit_amount = int(input("Please enter deposit_amount "))
            balance = balance + deposit_amount
            print("======================================")
            print("======================================")
            print(f"{deposit_amount} is credit from your account")
            print("======================================")
            print("======================================")
            print(f"your current balance is {balance}")
            print("======================================")
            print("======================================")
        if option == 4:
            break

else:
    print("Wrong pin Please try again")
