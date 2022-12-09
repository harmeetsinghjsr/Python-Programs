import datetime
import sys

# using try-except blocks for handling the exceptions
def validateDate(date):
   check = True
   try:
   # It returns true if the date is correctly formatted else it will go to except block
    datetime.datetime.strptime(date, '%d/%m/%Y')

   # If the date validation goes wrong
   except ValueError:
     check = False

   return check

def userInput():
    global startDate
    global endDate

    startDate =input("Enter the start date in given format of DD/MM/YYYY: ")
    if(validateDate(startDate)):
      print("The Start date is recorded")
    else:
      print("The format is incorrect please check it........")
      sys.exit()

    endDate =input("Enter the end date in given format of DD/MM/YYYY: ")
    if(validateDate(endDate)):
        print("The End date is recorded")
    else:
        print("The format is incorrect please check it........")
        sys.exit()

def findLeapYear(start, end):
    #Checking whether end year is greater than start or not.....
    while start >= end:
      print("Check your year input again..... The end date year should be grater than the start date year.........")
      sys.exit()

    global leapYear,nonLeapYear

    #Checking leap year or not and appending it to the list....
    while start <= end:
     if (start % 4 == 0 and start % 100 != 0) or (start % 100 == 0 and start % 400 == 0) :
        leapYears.append(str(start))
     else:
        nonLeapYears.append(str(start))
     start += 1



#Decalring start date and end date variables
startDate = ""
endDate = ""

#Taking User input and validating the date
userInput()

#Extracting Year from the entered date
startYear = int(datetime.datetime.strptime(startDate, '%d/%m/%Y').year)
endYear = int(datetime.datetime.strptime(endDate, '%d/%m/%Y').year)

#Declaring list to contain leap and non leap years seperately
leapYears = []
nonLeapYears = []

#Calling the main function
findLeapYear(startYear,endYear)

#Printing th list in appropraite format
print("\nLeap years are:")

for line in range(0, len(leapYears), 10):
    print ("{0}.".format(", ".join(leapYears[line:line+10])))

print("\nNon Leap years are:")
for line in range(0, len(nonLeapYears), 10):
    print ("{0}.".format(", ".join(nonLeapYears[line:line+10])))
