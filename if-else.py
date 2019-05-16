#IF, ELSE
sunny = True
if sunny:
    print("It's sunny")
    print("It's too sunny")
    print("It's too much sunny")
else:
    print("It's not sunny")
    print("It's not sunny at all")

#IF, ELSE & ELIF
num = 4
if num > 10:
    print("num > 10")
elif num > 5:
    print("5 < num <= 10")
elif num > 2 and num%2==0:
    print("it's 4")
else:
    print("num <= 5")


year = 2020
if year%4==0 or year%100==0:
    print("leap year")
else:
    print("not leap year")

if 8:
    print("it's 8")
if 0:
    print("it's 0. wont be printed")
if -2:
    print("it's -2")
if None:
    print("it's none. wont be printed")


if "neha":
    print("its neha")
if "":
    print("its empty. wont be printed")
