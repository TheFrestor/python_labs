def linear_search(nums, x):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    else: return -1

def binary_search(sorted_nums, x):
    lo,hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo+hi)//2
        if sorted_nums[mid] == x: return mid
        elif x > sorted_nums[mid]: 
            lo = mid +1
        elif x < sorted_nums[mid]:
            hi = mid -1
    return -1

def two_sum_brute(nums, target):
    for i in range(len(nums)-1):
        x = target - nums[i]
        for j in range(i+1,len(nums)):
            if nums[j] == x: return (i,j)
    return None 

def two_sum_fast(nums, target):
    find_dict = {}
    for i in range(len(nums)):
        x = target - nums[i]
        if x in find_dict: return find_dict[x],i
        else: find_dict[nums[i]] = i
    return None 