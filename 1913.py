def main(nums):
    nums.sort()
    return nums[-1] * nums[-2] - nums[1] * nums[0]
