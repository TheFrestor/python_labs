min_max_tuple = tuple((float(x) if "." in x else int(x) for x in input().split(",")))
if len(min_max_tuple) == 0:
    print("ValueError")
else:
    print(min(min_max_tuple), max(min_max_tuple))

    
    


