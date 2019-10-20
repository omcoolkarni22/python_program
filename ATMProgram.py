bal=1000
pin=1560
def withdraw():
    withd=int(input("\nEnter the amount to be withdrawn: "))
    if withd > bal:
        print("\nEnter amount less than ",bal)
        withdraw()
    else:
        print("\nThank You for using our service ")
        print("\nAvailable Balance after withdrawl ",(bal-withd))
        main()
def Addmoney():
    addd=int(input("\nEnter the amount to be added "))
    global bal #taking bal as global
    bal=bal+addd
    print("\nUpdated Balance is ",bal)
    main()

def CheckBalance():
    print("\nAvailable Balance in your Account is ",bal)
    main()



def main():
    npin=int(input("\n***WELCOME*** User\nPlease enter your pin(4 digit pin): \n"))
    if pin==npin:
        choice=int(input("\n1.Withdraw\n2.Addmoney\n3.Check Balance\n4.Exit\n"))
        if choice==1:
            withdraw()
        elif choice==2:
            Addmoney()
        elif choice==3:
            CheckBalance()
        elif choice==4:
            exit()
        else:   
            print("\nPlease enter a valid choice")
    else:
        print("\nCrediantial Error")
        main()
main()

