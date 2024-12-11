def count_number_of_increases_cy(nums):
    cdef int current_num, count, num, i
    cdef int n = len(nums)
    current_num = nums[0]
    count = 0     
    for i in range(1, n):
        num = nums[i]
        if num > current_num:
            count += 1
        current_num = num  
    return count
