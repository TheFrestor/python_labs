def bubble_sort(nums):
    nums2 = nums.copy()
    for i in range(len(nums)-1):
        Flag = True
        for j in range(len(nums)-1 - i):
            if nums2[j] > nums2[j+1]:
                Flag = False
                first_digit = nums2[j] 
                second_digit = nums2[j+1] 
                nums2[j] = second_digit
                nums2[j+1] = first_digit
        if Flag == True: break
    return nums2

def insertion_sort(nums):
    nums2 = nums.copy()
    for i in range(1,len(nums)):
        current = nums2[i]
        j = i - 1
        while j >= 0 and nums2[j] > current:
            nums2[j + 1] = nums2[j]
            j -= 1
        nums2[j + 1] = current
    return nums2   

def selection_sort(nums):
    nums2 = nums.copy()
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums2[min_index] > nums2[j]: min_index = j
        first_digit = nums2[min_index]
        second_digit = nums2[i] 
        nums2[min_index] = second_digit
        nums2[i] = first_digit
    return nums2