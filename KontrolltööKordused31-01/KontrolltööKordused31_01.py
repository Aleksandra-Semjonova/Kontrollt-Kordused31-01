#1
n=int(input())
for i in range(n):
    print(" /V\\n / V \\n / V V \\n /VV V VV\ ")
for j in range(1,9):
    for i in range(1,9):
        print(i,end="/V\\n / V \\n / V V \\n /VV V VV\ ")
    print()

#4
n= int(input("sisestage suur arv: "))
paaritu= 0 
veider= 0
for i in n: 
    if i % 2 == 0:
        paaritu += 1
    else:
        veider += 1
print("paaritu number: " str(paaritu))
print("veider number: " str(veider))