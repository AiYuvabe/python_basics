# -*- coding: utf-8 -*-
"""6_DataTypes_Numbers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zclbmVQT0TkB0-eO2_2RClGtfKpJDx5t

##2. Numbers
Python supports various numerical types:

- Integers (int): Whole numbers (e.g., 10, -3).
- Floats (float): Decimal numbers (e.g., 3.14, -2.5).

```
# Examples of numbers
age = 25  # Integer
height = 5.9  # Float
```

##Common Operations

### Arithmetic Operations

```
a = 10
b = 3

# Addition
print("Addition (a + b):", a + b)  # Output: 13

# Subtraction
print("Subtraction (a - b):", a - b)  # Output: 7

# Multiplication
print("Multiplication (a * b):", a * b)  # Output: 30

# Division
print("Division (a / b):", a / b)  # Output: 3.3333333333333335

# Floor Division
print("Floor Division (a // b):", a // b)  # Output: 3

# Modulus
print("Modulus (a % b):", a % b)  # Output: 1

# Exponentiation
print("Exponentiation (a ** b):", a ** b)  # Output: 1000

##Understanding Type Conversion in Python: int, str, and float

Type conversion in Python is a process of converting one data type to another. It is particularly useful when you need to process different data types, such as numbers and strings, together. Let's explore type conversion between integers (int), strings (str), and floating-point numbers (float), with examples.
"""

# Type Conversion
num_str = "42"

# Convert string to integer
num_int = int(num_str)
print("String to Integer:", num_int)  # Output: 42

# Convert integer to float
num_float = float(num_int)
print("Integer to Float:", num_float)  # Output: 42.0

"""##1. Converting a String to an Integer (str to int)
Strings often contain numeric characters (e.g., "42") that can be converted into integers. This is done using the int() function.

**Example:**
"""

num_str = "42"  # String containing a numeric value
num_int = int(num_str)  # Convert to integer
print("String to Integer:", num_int)  # Output: 42

"""- Key Points:
The string must represent a valid number; otherwise, Python will raise a ValueError.
"""

invalid_str = "forty-two"
num_int = int(invalid_str)  # This will raise ValueError

"""## 2. Converting an Integer to a String (int to str)
When you need to treat numbers as strings (e.g., concatenating numbers with text), use the str() function.

**Example:**
"""

num_int = 42  # An integer
num_str = str(num_int)  # Convert to string
print("Integer to String:", num_str)  # Output: "42"

"""**Use Case:**"""

age = 25
message = "I am " + str(age) + " years old."
print(message)  # Output: "I am 25 years old."

"""## 3. Converting an Integer to a Float (int to float)

You can convert an integer to a floating-point number using the float() function. This is often useful in mathematical operations where precision is required.

**Example:**
"""

num_int = 42
num_float = float(num_int)  # Convert to float
print("Integer to Float:", num_float)  # Output: 42.0

"""##4. Converting a Float to an Integer (float to int)
You can also convert floating-point numbers to integers using the int() function. Note that this process truncates the decimal portion.

**Example:**

##Understanding and Practicing the input() Function in Python

The input() function is one of the most basic and powerful tools in Python for interacting with users. It allows a program to take user input during execution, making the program dynamic and flexible.

###Key Concepts

###1. How It Works:

- The input() function waits for the user to type something and hit Enter.
- It always returns the user input as a string.

**Example:**
"""

name = input("What is your name? ")
print("Hello, " + name + "!")

num_float = 42.8
num_int = int(num_float)  # Convert to integer
print("Float to Integer:", num_int)  # Output: 42

"""###2. Basic Syntax:
- variable = input(prompt)
- prompt: A message displayed to the user before they input data.

## Exercises for Practicing input()
"""

# 1. Basic Input Practice
# Write a program that asks the user for:

# Their name
# Their favorite color
# Their age
# Then print a message like:

#Hello [Name]! Your favorite color is [Color], and you are [Age] years old.

name = input("Enter your name")
favorite_color = input ("What is your favorite color")
age = input ("What is your age")

print(f"Hello {name} ! Your favorite color is {favorite_color}, and you are {age} old.")

"""###Now that we have understood datatype conversion its time to practice:"""

#1. Problem Statement: Reads a user's age as a string. Then calculate how many years it will take for the user to turn 100 and print that

age = int (input ("What is your age : "))
total_year = 100
years_to_user_turn_100 = total_year - age
print(f"it will take {years_to_user_turn_100} for the user to turn 100")

# Write a program that:

# Asks the user for two numbers.
# Prints their sum, difference, product, and quotient.

number = int(input("Enter the number : "))
number1 = int(input("Enter the number 2 : "))

sum = number + number1
print(sum)
difference = number - number1
print(difference)
product = number * number1
print(product)
quotient = number / number1
print(quotient)

"""###Debugging Exercise
The following program has an error. Fix it:
"""

number = input("Enter a number: ")
result = number * 2
print("Double the number is:", result)

number = int(input("Enter a number: "))
result = number * 2
print("Double the number is:", result)

"""###Calculation Exercise: 1"""

#Circumference Calculation: Calculate the circumference of a circle for an input radius
PI = 3.14
#Forumala for circumference: = 2 * PI * r
#Expected outout: The circumference of circle with radius (radius) is (circumference)

radius = int(input ("Enter the radius : "))
PI = 3.14
circumference = 2 * PI * radius
print(f"The circumference of circle with radius {radius} is {circumference}")

"""###Calculation Exercise: 2"""

#Area of a square: Ask user for the dimension of the length of one side of a square.
# Calculate and print its area
#Expected output: The area of a square with length of side (length) is (area)

area = int (input("Enter the length : "))
length = int (input("Enter the area : "))
expected_output = area * length
print(expected_output)

"""##Comparison Operators

We discussed comparision operators [here](https://colab.research.google.com/drive/12vQ_fYgTXlbqeQvAlQLmSyAd7roQgcaC#comp_operators)

Please refer the text to answer the questions below
"""

# 1. Simple Comparisons
# Write a program that:

# Asks the user to input two numbers.
# Compares the numbers using all the comparison operators (==, !=, >, <, >=, <=).
# Prints the result of each comparison.

#Assuming number1 is 5 and number 2 is 10 the expected output shall be:

number1 =int(input("Enter the number"))
number2 =int(input("Enter the number"))

result = number1 == number2
print(result)
result = number1 != number2
print(result)
result = number1 > number2
print(result)
result = number1 < number2
print(result)
result = number1 >= number2
print(result)
result = number1 <= number2
print(result)


#Repeat this by entering number1 = 10 and number2 = 5
#Repeat this by entering number1 = 10 and number2 = 10

# 2. Age Verification
# Write a program that:

# Asks the user for their name and age.
# Checks if the user is old enough to drive, vote, or drink (based on common age thresholds).
# Prints messages based on their age.
MINIMUM_AGE_TO_DRIVE = 16
MINIMUM_AGE_TO_VOTE = 18
MINIMUM_AGE_TO_DRINK = 25

#Expected outout:
#Hello {name}
#You are old enough to drive: True
#You are old enough to vote: False
#You are old enough to drink: False

name = input("Enter your name : ")
age = int(input("What is your age : "))
MINIMUM_AGE_TO_DRIVE = 16
MINIMUM_AGE_TO_VOTE = 18
MINIMUM_AGE_TO_DRINK = 25
eligibility_to_drive = MINIMUM_AGE_TO_DRIVE<age
eligibility_to_vote = MINIMUM_AGE_TO_VOTE<age
eligibility_to_drink = MINIMUM_AGE_TO_DRINK<age
print(f"Hello {name} You are old enough to drive : {eligibility_to_drive}")
print(f"Hello {name} You are old enough to drive : {eligibility_to_vote}")
print(f"Hello {name} You are old enough to drive : {eligibility_to_drink}")

#3. Case-Sensitive Comparison
# Write a program that:
# Asks the user to input two words.
# Compares the words using >, < == and != and prints the result.
#Expected outout:
#{word1} > {word2}: True
#{word1} < {word2}: False
#{word1} == {word2}: False
#{word1} != {word2}: False

#Please run the above exercise with these combination of words:

#Run 1: hello, bye
#Run 2: a, b
#Run 3: B, a
#Run 4: Hello, hello
#Run 5: H, h

word1 = input("Enter word 1: ")
word2 = input("Enter word 2: ")
print(word1 > word2)
print(word1 < word2)
print(word1 == word2)
print(word1 != word2)

# 4. Password Length Check
# Write a program that:

# Asks the user to input a password.
# Checks if the password length is at least 8 characters
# Expected output if password length is >=8 : Password {password} is valid: True
# Expected output if password length is <8 : Password {password} is valid: False

password = input("Enter password")
MINIMUM_LENGTH_OF_PASSWORD = 8
result = len(password)>MINIMUM_LENGTH_OF_PASSWORD
print(f"Password : {password} is valid: {result}")

#5. Write a program that:

# Following is the price of apple and bananas per kilogram.
price_apples = 185.50
price_bananas = 78.12

# Asks the user to input their shopping budget.
# Asks the user to input how many kgs of apples and bananas they want to buy

# Compares the budget to the total bill and inform whther they are over or under budget.
#Expected outout. Your budget: {budget}, Bill: {shopping_bill}. Over budget: True

budget = int(input("Enter your budget "))
apple_in_kg = int(input("How many kgs of apple you want "))
banana_in_kg = int(input("How many kgs of apple you want "))
price_apples = 185.50
price_bananas = 78.12
total_cost = (apple_in_kg*price_apples) + (banana_in_kg*price_bananas)
print(f"Your budget : {budget}, Bill: {total_cost}. Over_budget: {total_cost>budget}")

