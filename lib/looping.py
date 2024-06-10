#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")


happy_new_year()
       

def square_integers(int_list):
    squared_no = [x**2 for x in int_list]   
    return squared_no

numbers = [2,4,6,8]
square_no = square_integers(numbers)
print(square_no)

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz()


