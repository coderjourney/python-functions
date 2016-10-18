# f(x) = x + 1

def f(x):
    return x + 1

# Fizz Buzz
# "Fizz" if a number is divisible by 3
# "Buzz" if the number is divisible by 5
# "Fizz Buzz" if it's divisible by both
# otherwise we're going to print the number itself

def fizz_buzz(limit):
    for num in range(1, limit):
        output = ""
        if num % 3 == 0: output += "Fizz "
        if num % 5 == 0: output += "Buzz"
        print(output or num)

def fizz_buzz2(limit=20):
    fizz_buzz(limit)

def fizz_buzz3(limit, fizz="Fizz", buzz="Buzz"):
    for num in range(1, limit):
        output = ""
        if num % 3 == 0: output += fizz + " "
        if num % 5 == 0: output += buzz
        print(output or num)
