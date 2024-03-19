def twoSum(nums, target: int):
    cal_dict = {}

    for i, n in enumerate(nums):

        diff = target - n
        if diff in cal_dict:
            return [cal_dict[diff], i]
        cal_dict[n] = i
    return


nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1))
