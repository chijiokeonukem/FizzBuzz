# Write a program that prints the numbers from 1 to 100 each on it's own line. 
# But for multiples of three print "Fizz" instead of the number and for the 
# multiples of five print Buzz". 
#
# For numbers which are multiples of both three and five print "FizzBuzz".

def fizzbuzz():
    for k in range(1, 101):
        if (k % 3 == 0 and k % 5 == 0):
            print("FizzBuzz")
        elif(k % 3 == 0):
            print("Fizz")
        elif(k % 5 == 0):
            print("Buzz")
        else:
            print(k)

fizzbuzz()
