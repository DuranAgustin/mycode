#!/usr/bin/env python3
def main():
   message = "Enter numberic score to get a letter grade"
   grade = int(input("Enter a number 0-100: "))
   if grade > 100 or grade < 0:
       print("Invalid grade inserted: " ,grade)
   elif grade >= 90:
       print("You got an A with: ",grade)
   elif grade >= 80:
       print("You got a B with: ", grade)
   elif grade >= 70:
       print("You got a C with: ", grade)
   elif grade >= 60:
       print("You got a D with: ", grade)
   else:
       print("you got an F with: ", grade)
main()

