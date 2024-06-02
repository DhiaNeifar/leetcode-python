def main(nums):
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == 0:
            return nums[j]
        if nums[i] + nums[j] > 0:
            j -= 1
        if nums[i] + nums[j] < 0:
            i += 1
    return -1


if __name__ == '__main__':
    nums_ = [-10, 8, 6, 7, -2, -3]
    print(main(nums_))
