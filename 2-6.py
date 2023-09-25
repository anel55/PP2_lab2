a, b, c = int(input()), int(input()), int(input())
tup = (a, b, c)
if len(set(tup)) == 3:
    print(0)
elif len(set(tup)) == 2:
    print(2)
else:
    print(3)
