# ---------------------------
# CASTING DATA TYPES
# ---------------------------

# cast from str to int
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is", type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is", type(str_numbers_to_int))

print("-" * 40)

# casting from int to str
integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is", type(integer_to_str))

print("-" * 40)

# casting from int to bool
num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))

num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))

print("=" * 50)

# ---------------------------
# COMPARISON OPERATORS
# ---------------------------

print("8 == 8 ->", 8 == 8)
print("8 != 9 ->", 8 != 9)
print("8 > 9  ->", 8 > 9)
print("8 < 9  ->", 8 < 9)
print("8 <= 9 ->", 8 <= 9)
print("9 >= 9 ->", 9 >= 9)

print("=" * 50)

# ---------------------------
# LOGICAL OPERATORS
# ---------------------------

a = True
b = True
print("a and b ->", a and b)
print("a or b  ->", a or b)
print("not b   ->", not b)

# logic expression
print("5 > 6 or 6 < 7 ->", 5 > 6 or 6 < 7)

print("=" * 50)

# ---------------------------
# ARITHMETIC OPERATORS
# ---------------------------

e = 8
f = 2

# Summation
sum = e + f
print(f"The sum of e with f is : {sum}\n")

# Reduction
red = e - f
print(f"The reduction of e with f is : {red}\n")

# Multiplication
multi = e * f
print(f"The multiplication of e with f is : {multi}\n")

# Division
divi = e / f
print(f"The quotient of e with f is : {divi}\n")

# Modulo
mod = e % f
print(f"The remainder of e with f is : {mod}\n")

# Power
pow = e ** f
print(f"The power of e of f is : {pow}\n")

print("=" * 50)

# ---------------------------
# INPUT & OUTPUT
# ---------------------------

# Input
name = str(input("What is your name : "))
age = int(input("What's your age : "))

# Output
print("Name: ", name)
print("Age: ", age)

# Normal print
print('Hi all! I am', name, 'age', age, 'years old')

# Format print (f-string)
print(f'Hi all! I am {name} age {age} years old')

# Format print with % formatting
print('Hi all! I am %s age %d years old' % (name, age))