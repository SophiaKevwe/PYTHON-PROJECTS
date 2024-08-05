# BINARY GAP
# num = int(input("Enter a positive number: "))
# num = bin(num)
# num = num[2:]
# g = 0
# h = []
# a = (num.split("1"))
# for x in a:
#     h.append(len(x))
# c = max(h)
# t = h.index(c)
# for x in a:
#     if len(x) == c:
#         g = c
# if num[-1] == "0" and h[t] == h[-1]:
#     for t in a[-1]:
#         g = g - 1
# if g == 0:
#     h.remove(c)
#     c = max(h)
#     for x in a:
#         if len(x) == c:
#             g = c
# print(f"The number of binary gap in {num} is {g}")
num = int(input("Enter a positive number: "))
numm = bin(num)[2:].split("1")
if numm[-1] == "":
    numm.pop()
maxnum = 0
for t in numm:
    noz = t.count("0")
    if noz > maxnum:
        maxnum = noz
print(f"The number of binary gap in {num} is {maxnum}")


