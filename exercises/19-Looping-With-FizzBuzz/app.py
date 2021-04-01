def fizz_buzz():
    # your code here
    for i in range(1,101):
        multi3= i%3
        multi5= i%5
        if multi3 == 0 and multi5 == 0:
            print("FizzBuzz")
        elif multi3 == 0:
            print("Fizz")
        elif multi5 == 0:
             print("Buzz")
        else:
            print(i)

    return i

fizz_buzz()