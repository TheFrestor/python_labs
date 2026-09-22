unique_sorted = sorted(set((float(x) if "." in x else int(x) for x in input().split(","))))
if len(unique_sorted) == 0:
    print("")
else:
    print(unique_sorted)

    