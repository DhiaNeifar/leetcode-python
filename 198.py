def main(nums):
    if len(nums) < 3:
        return max(nums)
    result = 0
    curr_max = nums[-1]
    for i in range(len(nums) - 3, -1, -1):
        result = max(result, curr_max + nums[i])
        curr_max = max(curr_max, nums[i + 2])

    return result


if __name__ == '__main__':
    _nums = [2, 7, 9, 3, 1]
    print(main(_nums))
