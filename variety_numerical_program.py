print("this is the list of programs:")
print("1 - bigger number")
print("2 - lower number")
print("3 - equal number")
print("4 - not equal number")
print("5 - addition number")
print("6 - subtraction number")
print("7 - multiplication number")
print("8 - division number")

user_input = int(input("where do you want to proceed?: "))

num1 = int(input("insert a 1st number here: "))
num2 = int(input("insert a 2nd number here: "))

# Create a program that ask user to input 2 numbers. Print the bigger number.

def find_big_num(num1, num2):
    
    if num1 > num2:
        print(f"the biggest number is {num1}")
    else:
        print(f"the biggest number is {num2}")
    
# Create a program that ask user to input 2 numbers. Print the lower number.

def find_low_num(num1, num2):
    
    if num1 > num2:
        print(f"the lowest number is {num2}")
    else:
        print(f"the lowest number is {num1}")

# Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

def find_equal_num(num1, num2):

    if num1 == num2:
        print("Equal")
    else:
        print("Try Again!")

# Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

def find_not_equal_num(num1, num2):

    if num1 != num2:
        print("Not Equal")
    else:
        print("Try Again!")

# Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

def find_sum_of_num(num1, num2):

    sum = num1 + num2
    print(sum)
    
# Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

def find_diff_of_num(num1, num2):

    diff = num1 - num2
    print(diff)

# Create a program that ask user to input 2 numbers. Print the product of the two numbers.

def find_prod_of_num(num1, num2):

    prod = num1 * num2
    print(prod)

# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

def find_quot_of_num(num1, num2):

    quot = num1 // num2
    print(quot)
    
# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
# Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
# Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
# Create a program that ask user to input 10 numbers. Print the difference of all the numbers.
# Create a program that ask user to input 10 numbers. Print how many are odd numbers.
# Create a program that ask user to input 10 numbers. Print how many are even numbers.
# Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
# Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
# Create a program that ask user to input 2 numbers. When the first is greater than the second. Print all the numbers between the two.


if user_input == 1:
    result_big = find_big_num(num1, num2)
    print(f"{result_big}")

if user_input == 2:
    result_low = find_low_num(num1, num2)
    print(f"{result_low}")

if user_input == 3:
    result_equal = find_equal_num(num1, num2)
    print(f"{result_equal}")

if user_input == 4:
    result_not_equal = find_not_equal_num(num1, num2)
    print(f"{result_not_equal}")

if user_input == 5:
    result_sum = find_sum_of_num(num1, num2)
    print(f"{result_sum}")

if user_input == 6:
    result_diff = find_diff_of_num(num1, num2)
    print(f"{result_diff}")

if user_input == 7:
    result_prod = find_prod_of_num(num1, num2)
    print(f"{result_prod}")

if user_input == 8:
    result_quot = find_quot_of_num(num1, num2)
    print(f"{result_quot}")