def max_min(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
    return min(nums), max(nums)

#print(max_min(eval(input())))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

#print(unique_sorted(eval(input())))

def flatten(mat: list[list | tuple]) -> list:
    res = []
    for i in mat:
        if type(i) is not list and type(i) is not tuple:
            raise TypeError("строка не строка матрицы")
        res.extend(i)
    return res

print(flatten(eval(input())))