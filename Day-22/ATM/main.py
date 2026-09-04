import logic as lg

if lg.login():
    while True:
        lg.menu()
        ch = input("Enter your choice: ").upper()
        if ch == 'C':
            lg.checkbalance()
        elif ch == 'D':
            lg.deposit()
        elif ch == 'W':
            lg.withdraw()
        elif ch == 'V':
            lg.viewtransaction()
        elif ch == 'E':
            print("----------------Thankyou, Visit Again---------------")
            break
        else:
            print("Invalid choice. Please try again.")