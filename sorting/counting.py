def counting_sort(nums):
    counts = [0] * (max(nums) + 1)
    for i in range(len(nums)):
        counts[nums[i]] += 1
    output = []
    for i in range(len(counts)):
        if counts[i] != 0:
            for k in range(counts[i]):
                output.append(i)
    return output
