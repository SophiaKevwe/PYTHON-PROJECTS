#COLLATZ SEQUENCE
n = 1027371
while n != 1:
    print(n, end=", ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = n*3 + 1
print(n, end=".\n")

#NESTED LIST
# nl = [[2,3,4,5],[23,22,41,53],[5,6,1,6,4]]
# nlist=[]
# flist=[]
# for t in nl:
#     for k in t:
#         newk=k*2
#         nlist.append(newk)
#     flist.append(nlist)
# print(flist)
# nlist=[]

# adj = ["red","big","tasty"]
# fruits = ["apple","banana","cherry"]
# for x in adj:
#     for y in fruits:
#         print(x,y)
