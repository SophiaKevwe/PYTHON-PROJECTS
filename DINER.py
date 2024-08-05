def swaa(swa, ans, bi):
    if swa.upper() == "FUFU":
        n = 50 * ans
        bi = bi + n
    elif swa.upper() == "GARRI":
        n = 70 * ans
        bi = bi + n
    elif swa.upper() == "POUNDED YAM":
        n = 100 * ans
        bi = bi + n
    else:
        print("I'm sorry that's not among our menu, please try again.")
        saa = input("What swallow would you like: ")
        anhs = int(input(f"How many wraps of {saa} would you like to have: "))
        bi = swaa(saa, anhs, bi)
    return bi


def soupp(sou, bl):
    a = 0
    if sou.upper() == "EGUSI" or sou.upper() == "OKRO":
        bl = bl + 200
        a = 200
        print(f"Bill = {bl}")
    elif sou.upper() == "MIXED":
        bl = bl + 300
        a = 300
        print(f"Bill = {bl}")
    else:
        print("I'm sorry that's not among our menu, please try again.")
        soup = input("What soup would you like: ")
        sou = soup
        a, bl = soupp(soup, bl)
    return a, bl


def protein(prot, ans, bill, a):
    if prot.upper() == "MEAT":
        bill = bill + (100 * ans)
        a = a + 100
    elif prot.upper() == "FISH":
        bill = bill + (150 * ans)
        a = a + 150
    elif prot.upper() == "NONE":
        bill = bill
        a = a + 0
    else:
        print("I'm sorry that's not among our menu, please try again.")
        prote = input("What protein would you like, meat fish or none: ")
        if prote.upper() == "MEAT" or prote.upper() == "FISH":
            anns = int(input(f"How many {prote} would you like to have: "))
        else:
            anns = 0
        a, bill = protein(prote, anns, bill, a)
    return a, bill


def mainn():
    print("Welcome to Mama Joy's kitchen")
    name = input("Please enter your name: ")
    name = list(name)
    name[0] = name[0].upper()
    name = ("".join(name))
    print(f"HERE'S THE MENU {name}")
    print("SWALLOW: FUFU N50 \t GARRI N70 \t POUNDED YAM N100")
    print("SOUP:EGUSI N200 \t OKRO N200 \t MIXED N300 \nPROTEIN: MEAT N100 \t FISH N150")
    pla = input("Do you want to place an order (Y/N): ")
    if pla.upper() == "Y":
        swa = input("What swallow would you like: ")
        ans = int(input(f"How many wraps of {swa} would you like to have: "))
        bill = 0
        bill = swaa(swa, ans, bill)
        ansk = input("Would you like to add another swallow (Y/N): ")
        if ansk.upper() == "N":
            print(f"SWALLOW: {bill} \nPROCEED")
        else:
            print("Okay then.")
            sha = input("What swallow would you like: ")
            ahs = int(input(f"How many wraps of {sha} would you like to have: "))
            bill = swaa(sha, ahs, bill)
            print(f"SWALLOW: {bill} \nPROCEED")
        soup = input("What soup would you like: ")
        slllo, bill = soupp(soup, bill)
        print(f"SOUP: {slllo} \nPROCEED")
        prote = input("What protein would you like, meat fish or none: ")
        if prote.upper() == "MEAT" or prote.upper() == "FISH":
            anns = int(input(f"How many {prote} would you like to have: "))
            aa = 0
            p, bill = protein(prote, anns, bill, aa)
            anss = input("Would you like to add another protein (Y/N): ")
            if anss.upper() == "N":
                print(f"PROTEIN: {p} \nPROCEED")
                print(f"Your bill is {bill}")
            else:
                print("Okay then.")
                protee = input("What protein would you like, meat fish or none: ")
                if protee.upper() == "MEAT" or protee.upper() == "FISH":
                    anse = int(input(f"How many {protee} would you like to have: "))
                else:
                    anse = 0
                proteinp, bill = protein(protee, anse, bill, p)
                proteinp = proteinp * anse
                print(f"PROTEIN: {proteinp} \nPROCEED")
                print(f"Your bill is {bill}")
        elif prote.upper() == "NONE":
            anns = 0
            p = 0
            print(f"PROTEIN: {protein(prote, anns, bill, p)[0]} \nPROCEED \nYour bill is {bill}")
        else:
            protans = int(input(f"How many {prote} would you like to have: "))
            c = 0
            c, bill = protein(prote, protans, bill, c)
            protanss = input("Would you like to add another protein (Y/N): ")
            if protanss.upper() == "N":
                print(f"PROTEIN: {c} \nPROCEED")
                print(f"Your bill is {bill}")
            else:
                print("Okay then.")
                pret = input("What protein would you like, meat fish or none: ")
                if pret.upper() == "MEAT" or pret.upper() == "FISH":
                    anse = int(input(f"How many {pret} would you like to have: "))
                else:
                    anse = 0
                proteinpp, bill = protein(pret, anse, bill, c)
                print(f"PROTEIN: {proteinpp} \nPROCEED")
                print(f"Your bill is {bill}")
        cont = input(f"Thank you for your patronage {name},would you like to order again (Y/N): ")
        if cont.upper() == "Y":
            mainn()
        else:
            print(f"Thank you for your patronage {name}")
    else:
        print("Thank you for your time.")
mainn()
