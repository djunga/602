
# #Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# #The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.
def meal():
  meal = input("Please enter a meal:")
  if meal == "breakfast":
    print("How about some bacon and eggs?")
  elif meal == "lunch":
    print("How about a turkey sandwich?")
  elif meal == "dinner":
    print("How about chicken soup?")
  else:
    print("I got nothing")

meal()

# #Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20.
# #You should take in the user’s input for the number of hours worked, and their rate of pay.



def mail():
  employ_pay = float(input("Employee Pay: "))
  employ_hour =  float(input("Employee Hours: "))

  if employ_hour > 20:
    base = 20
    gross = (base * employ_pay) + ((employ_hour-base) * (1.5 * employ_pay))
    print(gross)
  else:
    print(employ_pay * employ_hour)

mail()

# # Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.

def times_ten(arg):
  return arg * 10


# Q4: Find the errors, debug the program, and then execute to show the output.

def main():    # Add a colon after the function name
      calories1 = input("How many calories are in the first food?")
      # change Calories1 -> calories1
      calories2 = input("How many calories are in the second food?")
      # change calories2 -> calories2
      showCalories(float(calories1), float(calories2))

def showCalories(c1, c2):   # Add a colon after the function name
   print("The total calories you ate today: {}".format(c1 + c2))

main()  # call the main function.

#Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
         #1/30 + 2/29 + 3/28 ............. + 30/1
from fractions import Fraction

numerator = 0
denominator = 31
sum = 0

while numerator < 30:
  numerator += 1
  denominator -= 1
  sum+=Fraction(numerator,denominator)

print(sum)



#Q6: Write a function that computes the area of a triangle given its base and height.
#The formula for an area of a triangle is:
#AREA = 1/2 * BASE * HEIGHT

#For example, if the base was 5 and the height was 4, the area would be 10.
#triangle_area(5, 4)   # should print 10

def area_triangle():
  base = int(input('What is the base of your triangle?'))
  height = int(input('What is the height of your traingle?'))
  print(f'The area of your triangle is {.5*base*height}')

area_triangle()
