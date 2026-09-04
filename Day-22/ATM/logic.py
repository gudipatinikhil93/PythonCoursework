data ={
    123456:{'name':"Nikhil",'pin':1234,'balance':99999,'history':[]},
    234561:{'name':"Prasad",'pin':1224,'balance':50000,'history':[]},
    345612:{'name':"Tharun",'pin':1244,'balance':100,'history':[]},
}

def login():
    global acc_num
    acc_num = int(input("Enter your account number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login successful.")
        return True
    else:
        print("Invalid Login")


def menu():
    print(f"Welcome to the ATM, {data[acc_num]['name']}")
    print('[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transaction')
    print('[E]xit')


def checkbalance():
    print(f'Hello {data[acc_num]["name"]},')
    print("Current Balance: ", data[acc_num]['balance'],end='\n\n')


def deposit():
    amount = int(input("Enter the amount to deposit:"))
    data[acc_num]["balance"] += amount
    data[acc_num]["history"].append(f"{amount}is deposited")
    print(f"{amount} is deposited successfully")
    checkbalance()


def withdraw():
    amount = int(input("Enter the amount to withdraw:"))
    if data[acc_num]["balance"] >= amount:
       data[acc_num]["balance"] -= amount
       data[acc_num]["history"].append(f"{amount} is withdrawn")
       print(f"{amount} is withdrawn successfully")
       checkbalance()
    else:
     print("Insufficient balance")


def viewtransaction():
    if data[acc_num]["history"]:
        print("===============Transaction History===============")
        for i in data[acc_num]["history"]:
            print(i)
        else:
            print("**********End of the History**********")
    else:
        print("No transaction history")
        