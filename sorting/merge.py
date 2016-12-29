def merge_sort(nums):
    if len(nums) == 1:
        return nums
    else:
        mid = len(nums) // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        return merge(left, right)

def merge(left, right):
    merged = []
    x, y = 0, 0
    while x < len(left) and y < len(right):
        if left[x] <= right[y]:
            merged.append(left[x])
            x += 1
        else:
            merged.append(right[y])
            y += 1
    while x < len(left):
        merged.append(left[x])
        x += 1
    while y < len(right):
        merged.append(right[y])
        y += 1
    return merged
