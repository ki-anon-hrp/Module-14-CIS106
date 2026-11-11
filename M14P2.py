# Kirill M14P2 11/10/2026

# Define a class
class Student:

# Define first method which define first name, last name, district code, and enrolled credits
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

# Define second method which finding price for specific district
    def tution_owed(self):
        if self.district_code == "I":
            rate = 250
        else: 
            rate = 500
        return rate * self.enrolled_credits

# Define what data we use in Stundent class 
student1 = Student('Peter', 'Parker', 'O', 15)

# Printing each value with specific method
print(student1.first_name)
print(student1.last_name)
print("Student district code:", student1.district_code)
print(student1.enrolled_credits)

# Using method tution_owed
print("Tution owed:", student1.tution_owed())