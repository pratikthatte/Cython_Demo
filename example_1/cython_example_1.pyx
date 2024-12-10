def count_number_of_increases_cy(nums):
    current_num = nums[0]
    count = 0
    for num in nums[1:]:
        if num > current_num:
            count += 1
        current_num = num
    return count