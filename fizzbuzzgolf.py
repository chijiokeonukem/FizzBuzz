for k in range(1, 101):
    if (k % 3 == 0 and k % 5 == 0):
        print("FizzBuzz")
    elif(k % 3 == 0):
        print("Fizz")
    else:
        print("Buzz") if (k % 5 == 0) else print(k)