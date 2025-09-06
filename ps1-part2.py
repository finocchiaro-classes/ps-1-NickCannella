def number_fun(a, b):
    print(f"You entered {a} and {b}")
    print(f"{a} + {b} = {a+b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} ** {b} = {a**b}")
    print(f"{a} % {b} = {a%b}")

firstnum = int(input("Select an interger between 10 and 100: "))
secondnum = int(input("Select an interger that is less than 4: "))

number_fun(firstnum, secondnum)
               
