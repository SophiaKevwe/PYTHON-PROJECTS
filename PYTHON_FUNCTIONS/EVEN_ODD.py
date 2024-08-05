def checkOddEven(n):
    evenSet = []
    oddset = []
    if n % 2 != 0:
        statement1 = (f"{n} is odd")
        for i in range(3, 31):
            oddset.append(i)
        if n in oddset:
            statement = (f"{n} is within the range of 3 and 30")
        else:
            statement = (f"{n} is not within this range")
    elif n % 2 == 0:
        statement1 = (f"{n} is even")
        for i in range(2, 21):
            evenSet.append(i)
        if n in evenSet:
            statement = (f"{n} is within the range of 2 and 20")
        else:
            statement = (f"{n} is not within this range")
    else:
        print("outside parameters")

    return (statement1, statement)



wantMore = "yes"
while wantMore == "yes":
    num = input("enter your number")
    num = int(num)
    if num % 2 != 0:
        print(f"{num} is an odd number")
    elif num % 2 == 0:
        print(f"{num} is an even number")
    wantMore = input("wanna continue")
