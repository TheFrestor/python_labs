def max_min(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
    else: 
        max_res = 0
        min_res = 9*10**10
        for i in nums:
            if i > max_res:
                max_res = i
            if i < min_res:
                min_res = i
    return (min_res, max_res)
print(max_min(eval(input())))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if len(nums) == 0: return []
    res = []
    for i in nums: 
        if i not in res:
            res.append(i)
    res1 = []
    for i 


#print(unique_sorted(eval(input())))

def flatten(mat: list[list | tuple]) -> list:
    res = []
    for i in mat:
        if type(i) is not list and type(i) is not tuple:
            raise TypeError("строка не строка матрицы")
        res.extend(i)
    return res

print(flatten(eval(input())))

