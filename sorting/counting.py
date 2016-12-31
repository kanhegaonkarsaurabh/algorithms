def counting_sort(nums):
    sorted_nums = []
    counts = [[] for i in range(max(nums) + 1)]
    for i in range(len(nums)):
        counts[nums[i]].append(nums[i])
    for i in range(len(counts)):
        if counts[i]:
            sorted_nums.extend(counts[i])
    return sorted_nums
