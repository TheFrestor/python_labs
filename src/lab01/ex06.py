n = int(input("in_1: "))
list1 = []
for i in range(n):
    fam, name, age, forma = input(f"in_{i+2}: ").split()
    list1.append([fam, name, age, forma])
ocn = 0
for i in range(n-1):
    if list1[i][3] == "True": ocn +=1
print(f"out: {ocn} {n - ocn}")