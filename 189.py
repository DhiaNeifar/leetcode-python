def main(nums, k):
    n = len(nums)
    for i in range(k):
        nums[n - k + i], nums[i] = nums[i], nums[n - k + i]
        nums[n - k + i], nums[n - k + i - 1] = nums[n - k + i - 1], nums[n - k + i]
    print(nums)
    pass


if __name__ == '__main__':
    nums_ = [-1, -100, 3, 99]
    k_ = 2
    main(nums_, k_)
