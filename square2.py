print("Hello World!")
print("Hello World, This is my first python class!")
message = "This is the message I want you to see"
print(message)

# Write a program that calculates the area of a square
# Write the formula: Length * Length
# Measure the length using a device
###############################################################################
# Convert your program to accept user input for the length variable and
# use the input to compute the area of the square
###############################################################################
# Ask the User for the length
# "Please enter the length of the square: " #######################################
######################################################################
# We are going to hardcode values; No dynamic values
length = 6
# Calculate the area of the square using the formula(Length * Length)
# Read up: Variable naming styles: length_of_square(Allowed) lengthOfSquare(Not)
area = length * length
print(area)

# pysimplegui

# Write a program that calculates the area of a square

num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   for i in range(1,num + 1):  
       factorial = factorial*i  
   print("The factorial of",num,"is",factorial) 



# Prime numbers

num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  
