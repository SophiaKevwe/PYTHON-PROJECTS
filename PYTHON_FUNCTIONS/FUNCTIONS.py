def say_hello():
    print("Hello!")


say_hello()

# f"" is used for formatting the print statement to make al the variables included turn to strings


def sayhello(name):
    print(f"Hello {name}!")


kevwe = 19
sayhello(kevwe)


def cal(*nam, **nm):
    print(nm)
    return sum(nam)


print(cal(1, 2, 3, 4, 5, num1=1, num2=2))


def add_two_num(a, b):
    return a+b


a = add_two_num(21, 48)
print(a)


def add_two_num(a, b):
    return(f"The sum of {a} and {b} is {a+b}")


b = add_two_num(2, 5)
print(b)


def fahrenheit(x):
    c = (x*(9/5))+32
    return c


cel = int(input("Enter a celsuis degree: "))
print(f"{cel} degree celsuis to fahrenheit is {fahrenheit(cel)} degrees fahrenheit")


def word_count(sent, l):
    i = 0
    for x in sent.lower():
        if l.lower() == x:
            i += 1
    return i


sentence = "I am a big car in a big gold blue farm"
letter = "a"
num = word_count(sentence, letter)
print(f"The number of times {letter} is used in the sentence '{sentence}' is {num}")

# LAMBDA FUNCTION TO WRITE A CODE ON ONE LINE
a = lambda x: x+2
print(a(5))








