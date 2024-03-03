class customer:
    def __init__(self, ac:int, name : str , bal : int):
        self.ac=ac
        self.name=name
        self.bal=bal
class Bank:
    def __init__(self):
        self.CustomerList=[]
        self.ac=1
    def addCust(self, name : str , bal : int):
        newCustomer=customer(self.ac,name,bal)
        self.CustomerList.append(newCustomer)
        self.ac+=1
    def display_less(self):
        for element in self.CustomerList:
            if element.bal<100:
                print(f"Name: {element.name} Account No. {element.ac}")
    def deposit_withdrawl(self,ac,amount,code:int):
        if code==1:
            self.CustomerList[ac-1].bal+=amount
        else:
            if self.CustomerList[ac-1].bal<amount:
                print("Insufficient Balance.")
            else:
                self.CustomerList[ac-1].bal-=amount
    def printall(self):
        for element in self.CustomerList:
            print(f"Ac/no.: {element.ac} Name : {element.name} Bal : {element.bal}")
Banker=Bank()
while True:
    n=int(input("Choose what you have to do. \n1. Create Account. \n2. Display all customers. \n3. Display accounts with less than 100Rs. \n4. Deposit or withdrawl. \n5. Exit \n"))
    match n:
        case 1:
            name=input("Enter Name of the customer.\t ")
            bal=int(input("Enter the initial balance. \t"))
            Banker.addCust(name,bal)
        case 2:
            Banker.printall()
        case 3:
            Banker.display_less()
        case 4:
            ac=int(input("Enter the account number. \t "))
            amount=int(input("Enter the amount. \t"))
            code=int(input("1 for deposit OR 0 for withdrawl \t"))
            Banker.deposit_withdrawl(ac,amount,code)
        case 5:
            exit(0)
