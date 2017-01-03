def selection_sort(nums):
    for i in range(len(nums) - 1):
        index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[index]:
                index = j
        temp = nums[i]
        nums[i] = nums[index]
        nums[index] = temp
