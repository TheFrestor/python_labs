s = [1,2,3,4,5]
target = 4
for i in range(len(s)-1):
    for j in range(i+1):
        if s[i] + s[j] == target: print(s[i],a[j])