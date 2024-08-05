spam = 0
while spam < 5:
    print("Hello World")
    spam = spam + 1
spam = "Hello World"
for i in range (5):
    print(spam)
    print(i)
odd = list(range(1,10,2))
print("ODD NUMBERS")
for x in odd:
    print(x)
odd = list(range(1,100,2))
b = sum(odd)
avg= b/len(odd)
print (avg)
even = list(range(0,100,2))
c = sum(even)
avgg= c/len(odd)
print (avgg)
odd = list(range(1,100,2))
summ = 0
for x in odd:
    summ = summ + x
    avggg = summ/len(odd)
print(avggg)
countdown = list(range(5,0,-1))
print (countdown)
while True:
    print("Please type your name")
    name = input()
    if name  == "KEVWE":
        break
print("Thank you!")
while True:
    print("Who are you?")
    name = input()
    if name != "Joe" :
        continue
    print("Hello, Joe. What is the password?")
    password = input()
    if password == "Swordfish":
        break
print("ACCCESS GRANTED!")
for i in range(10):
    ast= "*"
    print(ast*i)
i=0
while i < 11:
    ast = "*"
    print(ast*i)
    i+=1
k=10
for i in range(1,20,2):
    print(k*" "+ i*"*")
    k-=1
for s in range(2):
    print("         | |")
print("       *******")
