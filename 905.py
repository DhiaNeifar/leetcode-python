def main(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] % 2 == 1 and nums[j] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        if nums[i] % 2 == 0:
            i += 1
        if nums[j] % 2 == 1:
            j -= 1
    return nums


if __name__ == '__main__':
    main([0, 1, 2])
