import first_module as x

x.start()
x.human_check()
input_pin =int(input("enter your pin"))
x.autentication(input_pin)

choose =int(input("Would you like to change your default pin press 1 to change press 0 if not"))
if choose==1:
    x.pin_change()
else:
    pass

balance = 2000000
k=1
while k!=0:
    choice = int(input("enter 1 to widraw 2 to deposit 3 to check balance : "))
    if choice==1:
        i=5
        print("Withdrawal limit is 200,000 and you only have 2,000,000 ooo")
        while i != -1:
            withdrawal=int(input("enter amount to withdraw : "))
            if withdrawal>balance:
                print("insufficent balance","try again")
                continue
            elif withdrawal>200000:
                print("you have exceeded the withdrawal limit","try again")
                continue
            else:
                remain = balance-withdrawal
                print("withdrawal successful","you have successully withdrawed ",withdrawal)
                print("Account balance is ",remain)
                break
        i= i-1
    elif choice==2:
        deposit=int(input("enter amount to deposit : "))
        print("deposit is complete")
        remain=deposit + balance
        print("Account balance is ",remain)
    elif choice==3:
        print("accounct balance is ",balance)
    else:
        print("guy you typed nonsenses")
    to_continue=int(input("do you want to continue, to continue press 1 to exit press 0 : "))
    if to_continue==1:
        pass
    else:
        break
    k=k+1
    