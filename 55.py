def main(nums):
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if goal <= i + nums[i]:
            goal = i
    return goal <= 0


if __name__ == '__main__':
    nums_ = [0, 2, 3]
    print(main(nums_))
