# Kirill M14P1 11/10/2026

# Define a class
class Employee:

# Define first method of defindning email, rate, and pay
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapny.com'

# Define second method of finding bonus by using rate and pay 
    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b

# Define third method of finding final pay by additing bonus rate and intinial pay
    def compute_bonus(self, rate):
        a = float(self.pay) + self.bonus(rate)
        return a

# Define what data we use in Employee class
empl1 = Employee('Frank', 'Alvino', 60000.00)

# Printing each data for each method
print(empl1.email)
print(empl1.first)
print(empl1.last)
print(empl1.pay)

# Asking for entering bonus rate
rate = float(input("Enter bonus rate: "))

# Using bonus method for showing rate
print("Bonus:", empl1.bonus(rate))

# Using compute_bonus method for showing final pay
print("Final pay:", empl1.compute_bonus(rate))