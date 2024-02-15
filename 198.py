def main(nums):
    rob = [0 for _ in range(len(nums) + 2)]
    for i in range(2, len(rob)):
        rob[i] = max(rob[i - 2] + nums[i - 2], rob[i - 1])
    return rob[-1]


if __name__ == '__main__':
    _nums = [2, 1, 1, 2]
    print(main(_nums))
