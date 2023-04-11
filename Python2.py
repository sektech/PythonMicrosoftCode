from datetime import date
import sys

print("Today date is " +str( date.today()))

print(sys.argv)
print ("Welcome")
result  = input("Enter your name ")
print("Hello "+ result)

parsecs_input = input("enter the number of parsecs.")
lightyears = int(parsecs_input) * 3.26
print(str(parsecs_input) + " parsecs is " + str(lightyears) + " lightyears")