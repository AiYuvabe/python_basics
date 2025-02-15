# -*- coding: utf-8 -*-
"""4_Variables_and_Basic_Operators.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12vQ_fYgTXlbqeQvAlQLmSyAd7roQgcaC

#Variables and Basic Operators in Python

###Welcome to your second Python lesson! In this notebook, we will cover:

1. [What are Variables?](#variables)
2. [Naming Rules for Variables](#naming_rules)
3. [Assigning Values to Variables](#variable_assignment)
4. [Basic Operators](#basic_operators)

# What are Variables?
<a name="variables"></a>

A variable is like a container that holds data. It gives data a name, so you can refer to it later.

For example:

```
age = 25
name = "John"
```

Here:

- age is a variable storing the number 25.
- name is a variable storing the string "John".
"""

#Exercise: Do you remember the print function from the previous session?
#Create a variable with your name and print your name to the console using print

"""# Naming Rules for Variables?
<a name="naming_rules"></a>

Here are the rules for naming variables in Python:

- Variable names can only contain letters (a-z, A-Z), numbers (0-9), and underscores (_).
- Variable names cannot start with a number.
- Variable names are case-sensitive (Name and name are different).
- You cannot use Python keywords (like if, for, while) as variable names.

Valid examples:

```
my_age = 20
total_score = 99
```

Invalid examples:

python
Copy code

```
1st_place = "Gold"  # Cannot start with a number
for = 10            # 'for' is a Python keyword
```
"""

#Please fix these variable names so that the program runs without any errors.
#Explain why these are not valid variable names.
#Assign them a value using assignment operator = and print the values using the print function
1variable
3cats
0_value

variable-nam
my@var
data%size

my variable
user name

if
for
class
True
False

"""# 3. Assigning Values to Variables
<a name="variable_assignment"></a>

You can assign values to variables using the = operator:
```
x = 5
y = 10
name = "Alice"
```

You can also update the value of a variable:
```
x = 5
x = x + 10  # Now x is 15
```

# Assign multiple variables in one line
```
x, y, z = 5, 10, 15
```

##Exercise: Favorite Things.

1. Objective: Using print function display your name, favorite color, lucky number, and hobby.
"""

#Hint: print function was discussed in previous session.
print("PAwan")
print("Red")
print("2")
print("reading")

"""2.  Objective: Create variables for your name, favorite color, lucky number, and hobby. Using print function print the values of these variables."""

my_name = "Pawan"
fav_color = "Red"
lucky_number = "2"
hobby = "reading"
print(my_name)
print(fav_color)
print(lucky_number)
print(hobby)

###Create four variables: my_name, favorite_color, lucky_number, and favorite_hobby.

"""3. Objective: Reassign the above variables with name, favorite color, lucky number, and hobby of the person next to you and print the same.


"""

###Use the above variables and reassign the values
my_name = "Pawan"
fav_color = "Red"
lucky_number = "2"
hobby = "reading"
print(my_name)
print(fav_color)
print(lucky_number)
print(hobby)
my_name = "Aditya"
fav_color = "Blue"
lucky_number = "5"
hobby = "guitar"
print(my_name)
print(fav_color)
print(lucky_number)
print(hobby)

"""#4 Basic Operators
<a name="basic_operators"></a>
Python supports many operators to perform calculations and operations on variables.

##4.1. Arithmetic Operators

| Operator | Description           | Example       |
|----------|-----------------------|---------------|
| `+`      | Addition              | `x + y`       |
| `-`      | Subtraction           | `x - y`       |
| `*`      | Multiplication        | `x * y`       |
| `/`      | Division              | `x / y`       |
| `**`     | Exponentiation        | `x ** y` (x to the power of y) |
| `%`      | Modulus (Remainder)   | `x % y`       |

Example:

```
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333...
print(a % b)  # 1
print(a ** b) # 1000
```

##Exercise: Basic Math Operations

1. Objective: Reassign the number in following code snippet by adding, subtracting, multiplying, and dividing 5. Print the outout after each operation.
"""

number = 10
#Add your code after this line
number2= 5

number = number+number2
print(number)
number = number - number2
print(number)
number = number * number2
print(number)
number = number / number2
print(number)

"""2. Objective: Using basic math operators finish the following exercises."""

# Initialize the variables
a, b, c = 5, 7, 9

# Calculate the sum of a and b, and print the result
sum_result = a + b
print("Sum of a and b:", sum_result)  # Expected output: 12

# Calculate the difference between b and a, and print the result
difference_result = b - a
print("Difference between b and a:", difference_result)  # Expected output: 2

# Calculate the modulus (remainder) when sum_result is divided by difference_result, and print the result
modulus_result = sum_result % difference_result
print("Modulus of sum_result % difference_result:", modulus_result)  # Expected output: 0

# Calculate the product of a and b, and print the result
multiplication_result = a * b
print("Multiplication of a and b:", multiplication_result)  # Expected output: 35

"""## Exercise: Temperature Conversion.

Celsius (°C) and Fahrenheit (°F) are two scales used to measure temperature. They are commonly used in different parts of the world, and understanding their differences can help in various scientific and practical applications.

1. Objective: What is the temperature outside? Is it in celsius or fahrenheit? If it is in celcius convert it in fahrenheit.

The formula to convert Celsius to Fahrenheit is:

```
F = (C × 9 / 5 ) + 32

```
"""

temp_outside = float(input("What is the temperature outside ? "))
scale_temp = input("Enter F if it's fahrenheit or Enter C if it's Celslius").upper()
celcius = "C"
fahrenheit = "F"
if (scale_temp == celcius):
  result = (temp_outside * 9/5 ) + 32
  print(result)

"""2. Objective: Can you think of a country where temperature is measured in Fahrenheit (°F)? Find a city from that country and get its current temperature.

Convert that temperature to Celcius using formula:

```
C = (F − 32) × 5 / 9

```
"""

temp_outside = float(input("What is the temperature outside ? "))
scale_temp = input("Enter F if it's fahrenheit or Enter C if it's Celslius").upper()
celcius = "C"
fahrenheit = "F"
if (scale_temp == fahrenheit):
  result = (temp_outside -32)  * 5/9
  print(result)

"""<a name="comp_operators"></a>
##4.2 Comparison Operators
These are used to compare two values and return True or False.

| Operator | Description              | Example   |
|----------|--------------------------|-----------|
| `==`     | Equal to                 | `x == y`  |
| `!=`     | Not equal to             | `x != y`  |
| `>`      | Greater than             | `x > y`   |
| `<`      | Less than                | `x < y`   |
| `>=`     | Greater than or equal to | `x >= y`  |
| `<=`     | Less than or equal to    | `x <= y`  |

```
a = 10
b = 5
print(a == b)  # False
print(a > b)   # True
```

##4.3. Logical Operators
Used to combine multiple conditions:

- **and** (True if both conditions are true)
- **or** (True if at least one condition is true)
- **not** (Reverses the condition)

Example:

```
x = 10
print(x > 5 and x < 15)  # True
print(x > 5 or x < 5)    # True
print(not (x > 5))       # False
```

"""