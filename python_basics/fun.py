# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
def odd_even():
    print "Odd/Even:"
    for i in range(1,101):
        if i % 2 == 0:
            print "Number is {}. This is an even number.".format(i)
        else:
            print "Number is {}. This is an odd number.".format(i)
odd_even()
# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
# The function should multiply each value in the list by the second argument.
def multiply(arr, value):
    list_new = []
    for i in arr:
        list_new.append(i*value)
    return list_new
# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in the original list.
def layered_multiples(arr):
    print "Hacker Challenge:"
    new_arr = []
    for i in arr:
        new_item = []
        for j in range(1,i+1):
            new_item.append(1)
        new_arr.append(new_item)
    return new_arr
x = layered_multiples(multiply([2,4,5],3))
print x
