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

# Create a program that ask user to input 2 numbers. Print the bigger number.

def find_big_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))
    
    if num1 > num2:
        print(f"the biggest number is {num1}")
    else:
        print(f"the biggest number is {num2}")
    
# Create a program that ask user to input 2 numbers. Print the lower number.

def find_low_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))
    
    if num1 > num2:
        print(f"the lowest number is {num2}")
    else:
        print(f"the lowest number is {num1}")

# Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

def find_equal_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))

    if num1 == num2:
        print("Equal")
    else:
        print("Try Again!")

# Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

def find_not_equal_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))

    if num1 != num2:
        print("Not Equal")
    else:
        print("Try Again!")

# Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

def find_sum_of_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))

    sum = num1 + num2
    print(f"the answer is {sum}")
    
# Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

def find_diff_of_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))

    diff = num1 - num2
    print(f"the answer is {diff}")

# Create a program that ask user to input 2 numbers. Print the product of the two numbers.

def find_prod_of_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))

    prod = num1 * num2
    print(f"the answer is {prod}")

# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

def find_quot_of_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))

    quot = num1 // num2
    print(f"the answer is {quot}")
    
# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

def find_float_quot_of_num(numflo1, numflo2):
    numflo1 = float(input("Insert a 1st number here: "))
    numflo2 = float(input("Insert a 2nd number here: "))

    float_quot = numflo1 / numflo2
    print(f"the answer is {float_quot}")

# Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

def find_remain_quot_of_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))

    remain_quot = (num1 % num2)
    print(f"the answer is {remain_quot}")

# Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

def find_raised_of_num(num1, num2):
    num1 = int(input("insert a 1st number here: "))
    num2 = int(input("insert a 2nd number here: "))

    raised_num = (num1 ** num2)
    print(f"the answer is {raised_num}")

if user_input == 1:
    find_big_num()

elif user_input == 2:
    find_low_num()

elif user_input == 3:
    find_equal_num()

elif user_input == 4:
    find_not_equal_num()

elif user_input == 5:
    find_sum_of_num()

elif user_input == 6:
    find_diff_of_num()

elif user_input == 7:
    find_prod_of_num()

elif user_input == 8:
    find_quot_of_num()

elif user_input == 9:
    find_float_quot_of_num()

elif user_input == 11:
    find_remain_quot_of_num()

elif user_input == 12:
    find_raised_of_num()

else:
    print("please try again.")