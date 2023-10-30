# Age calculator
from datetime import datetime
# date input from user
date_input = input("Enter a date in the format dd-mm-yyyy: ")
date =(date_input.split("-"))

# checks for valid date input 
try:
    input_date = datetime(int(date[2]),int(date[1]),int(date[0]))
except IndexError:
    print("Enter a valid date")

# gets current date
current_date = datetime.now()
# finds difference between the two datetime objects in days
difference = (current_date-input_date).days
# converts the days to years
years_diff = difference//365
print(years_diff)




