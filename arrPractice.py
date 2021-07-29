def array123(nums):
    i = 0
    pattern = 0
    while (i < len(nums)):
        if (nums[i] == 1):
            pattern = 1
        elif (nums[i] == 2 and pattern == 1):
            pattern = 2
        elif (nums[i] == 3 and pattern == 2):
            return True
        else:
            pattern = 0
        i += 1

    return False

array123([1,1,2,3,1])