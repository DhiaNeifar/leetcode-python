def brute_force(nums):
    _max = 0
    for i in range(len(nums) - 1):
        element = nums[i]
        count = 1
        for j in range(i + 1, len(nums)):
            if nums[j] > element:
                element = nums[j]
                count += 1
        _max = max(_max, count)
    print(_max)
    return _max


def main(nums):

    pass


if __name__ == '__main__':
    _nums = [0, 1, 0, 3, 2, 3]
    brute_force(_nums)
    # main(_nums)
