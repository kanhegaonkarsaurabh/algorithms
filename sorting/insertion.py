def insertion_sort(nums):
    for k in range(1, len(nums)):
        if nums[k] < nums[k - 1]:
            i, j = k - 1, k
            while i >= 0 and nums[i] > nums[j]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i, j = i - 1, j - 1
    return nums
