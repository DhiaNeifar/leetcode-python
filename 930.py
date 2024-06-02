# Brute Force
def main(nums, goal):
    count = 0
    for i in range(len(nums)):
        sum_ = 0
        for j in range(i, len(nums)):
            sum_ += nums[j]
            if sum_ == goal:
                count += 1
            if sum_ > goal:
                break
    print(count)
    pass


def main1(nums, goal):
    def func(x):
        if x < 0:
            return 0
        result = 0
        l = 0
        curr, r = 0, 0
        for r in range(l, len(nums)):
            curr += nums[r]
            while curr > x:
                curr -= nums[l]
                l += 1
            result += r - l + 1
        return result

    return func(goal) - func(goal - 1)



if __name__ == '__main__':
    nums_ = [0, 0, 0, 0, 0]
    goal_ = 0
    main1(nums_, goal_)
