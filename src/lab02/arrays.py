import ast

def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError

    return min(nums), max(nums)


nums = ast.literal_eval(input())

print(f"Ввод: {min_max(nums)}")