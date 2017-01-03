def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
