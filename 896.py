def main1(nums):
    if len(nums) < 3:
        return True
    i = 1
    while i < len(nums) and nums[i] == nums[i - 1]:
        i += 1
    if i == len(nums):
        return True
    if nums[i] > nums[i - 1]:
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[j - 1]:
                return False
    if nums[i] < nums[i - 1]:
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[j - 1]:
                return False
    return True


def main(nums):
    asc, desc = False, False
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            asc = True
        if nums[i] < nums[i - 1]:
            desc = True
    return not (asc and desc)


if __name__ == '__main__':
    _nums = []
    main(_nums)
