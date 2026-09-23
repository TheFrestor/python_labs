n = input("in:")

for i in range(len(n)):
    if n[i].isupper():
        index1 = i
        break

for i in range(index1 +1 ,len(n)):
    if n[i].isdigit():
        index2 = i
        break
ras = index2 +1 - index1

slovo = "".join(n[i] for i in range(index1,len(n),ras))
print(f"out: {slovo}")
