"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType, salary, hourlyPay, hoursWorked, comissionType, bonusAmount, numberOfContracts, amountPerContract):
        self.name = name

        if contractType == "contract":
            contractType = Monthly(contractType, hourlyPay, hoursWorked)
            self.contractType = contractType.get_contractType()
            self.hourlyPay = hourlyPay
            self.hoursWorked = hoursWorked
        elif contractType == "monthly":
            contractType = SalaryContract(contractType, salary)
            self.contractType = contractType.get_contractType()
            self.salary = salary

        if comissionType == "bonus":
            comissionType = Bonus(comissionType, bonusAmount)
            self.comissionType = comissionType.get_comissionType()
            self.bonusAmount = bonusAmount
        elif comissionType == "contracts":
            comissionType = Contracts(comissionType, numberOfContracts, amountPerContract)
            self.comissionType = comissionType.get_comissionType()
            self.numberOfContracts = numberOfContracts
            self.amountPerContract = amountPerContract
        else:
            self.comissionType = None


    def get_pay(self):
        if self.contractType == "contract":
            pay = self.hourlyPay*self.hoursWorked
        else:
            pay = self.salary

        if self.comissionType == "contracts":
            comissions = self.numberOfContracts*self.amountPerContract
        elif self.comissionType == "bonus":
            comissions = self.bonusAmount
        else:
            comissions = 0

        return pay + comissions


    def __str__(self):
        if self.contractType == "monthly":
            a = (f"{self.name} works on a monthly salary of {self.salary}")
        elif self.contractType == "contract":
            a = (f"{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyPay}/hour")
        else:
            print("error somewhere")

        if self.comissionType == "bonus":
            b = (f" and receives a bonus commission of {self.bonusAmount}")
        elif self.comissionType == "contracts":
            b = (f" and receives a commission for {self.numberOfContracts} contract(s) at {self.amountPerContract}/contract")
        else:
            b = ""

        print(f"{a}{b}.  Their total pay is {self.get_pay()}.")
        return (f"{a}{b}.  Their total pay is {self.get_pay()}.")



class Contract():
    def __init__(self, contractType):
        self.contractType = contractType

    def get_contractType(self):
        return self.contractType

class Monthly(Contract):
    def __init__(self, contractType, hourlyPay, hoursWorked):
        super().__init__(contractType)
        self.hourlyPay = hourlyPay
        self.hoursWorked = hoursWorked

class SalaryContract(Contract):
    def __init__(self, contractType, salary):
        super().__init__(contractType)
        self.salary = salary


class Comission():
    def __init__(self, comissionType):
        self.comissionType = comissionType

    def get_comissionType(self):
        return self.comissionType

class Bonus(Comission):
    def __init__(self, comissionType, bonusAmount):
        super().__init__(comissionType)
        self.bonusAmount = bonusAmount

class Contracts(Comission):
    def __init__(self, comissionType, numberOfContracts, amountPerContract):
        super().__init__(comissionType)
        self.numberOfContracts = numberOfContracts
        self.amountPerContract = amountPerContract






# name, contractType, salary, hourlyPay, hoursWorked, comissionType, bonusAmount, numberOfContracts, amountPerContract

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 4000, None, None, None, None, None, None)
str(billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'contract', None, 25, 100, None, None, None, None)
str(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 3000, None, None, 'contracts', None, 4, 200)
str(renee)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'contract', None, 25, 150, 'contracts', None, 3, 220)
str(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000, None, None, 'bonus', 1500, None, None)
str(robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'contract', None, 30, 120, 'bonus', 600, None, None)
str(ariel)
