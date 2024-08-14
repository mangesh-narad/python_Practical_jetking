def remove_duplicates(nums):
    unique_nums = list(set(nums))
    return len(unique_nums)
array = [1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(array)
print("New array length is:", new_length)
