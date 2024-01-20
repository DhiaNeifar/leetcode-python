def main(nums):
    count = [1 for _ in range(len(nums))]
    _max = 1
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                count[j] = max(count[j], count[i] + 1)
                _max = max(_max, count[j])
    print(_max)
    print(count)
    return count


if __name__ == '__main__':
    _nums = [2, 2, 1, 5, 7, -50, 80]
    main(_nums)
