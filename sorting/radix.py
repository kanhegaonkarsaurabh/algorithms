import math

def digits(x):
    return int(math.log10(x)) + 1

def counting_sort(nums, exp, base):
    sorted_nums = []
    counts = [[] for i in range(base)]
    for i in range(len(nums)):
        index = (nums[i] % exp) // (exp // base)
        counts[index].append(nums[i])
    for i in range(len(counts)):
        sorted_nums.extend(counts[i])
    return sorted_nums

def radix_sort(nums):
    sorted_nums, base = nums, digits(max(nums))
    for i in range(base):
        exp = base ** (i + 1)
        sorted_nums = counting_sort(sorted_nums, exp, base)
    return sorted_nums
