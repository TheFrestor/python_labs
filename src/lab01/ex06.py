n = int(input())
list1 = []
for i in range(n):
    fam, name, age, forma = input().split()
    list1.append([fam, name, age, forma])
ocn = 0
for i in range(n-1):
    if list1[i][3] == "True": ocn +=1
print(ocn, n - ocn)