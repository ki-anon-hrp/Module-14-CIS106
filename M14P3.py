# Kirill M14P3 11/10/2026

# Define a class
class Student:

# Creating list of value for each distrcit code
    TUITION_RATES = {
        "I": 250,
        "O": 500,
        "X": 800,
        "G": 250,
    }

# Define first method which define first name, last name, district code, and enrolled credits
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

# Define second method which using specific district code price on amount of credits
    def tution_owed(self):
        rate = Student.TUITION_RATES.get(self.district_code)
        return rate * self.enrolled_credits

# Define data in the list 
students = [
    Student('Peter', 'Parker', 'G', 15),
    Student('Daisy', 'Smith', 'X', 12),
    Student('Wilson', 'White', 'I', 13),
    Student('John', 'Flower', 'O', 11),
]

# Printing final result for each student with each method
for list in students:
    print(f"{list.first_name} {list.last_name} | District: {list.district_code} | Credits: {list.enrolled_credits} | Tution: ${list.tution_owed():,.2f}")
