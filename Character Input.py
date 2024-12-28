import time
from datetime import datetime

name = input("Enter your name: ")
time.sleep(1)
age = int(input("Enter your age: "))
time.sleep(1)
current_year = datetime.now().year
year = int(current_year) - age + 100

print(name + " you will be 100 years old in the year " + str(year))