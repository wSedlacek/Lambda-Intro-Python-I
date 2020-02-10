# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.


def add(num1, num2):
    return num1 + num2


print(add(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"


def add_all(*argv):
    total = 0

    for num in argv:
        total += num

    return total


print(add_all(1))                    # Should print 1
print(add_all(1, 3))                 # Should print 4
print(add_all(1, 4, -12))            # Should print -7
print(add_all(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(add_all(*a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.


def add_with_default(num1, num2=1):
    return num1 + num2


print(add_with_default(1, 2))  # Should print 3
print(add_with_default(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

def print_args(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")


# Should print
# key: a, value: 12
# key: b, value: 30
print_args(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
print_args(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
print_args(**d)
