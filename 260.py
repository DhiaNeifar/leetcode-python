def main(nums):
    nums.sort()
    results = []
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        if j == i + 1:
            results.append(nums[i])
        i = j
    return results
    pass


if __name__ == '__main__':
    nums_ = [1, 2, 1, 3, 2, 5]
    main(nums_)
