from typing import List


def buildArray(self, nums: List[int]) -> List[int]:
    # return [nums[num] for num in nums]
    for i in range(len(nums)):
        print(f"i = {i}")
        print(f"nums[i] = {nums[i]} | nums[nums[i]] = {nums[nums[i]]}")
        nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
        print(nums)
    return nums

if __name__ == '__main__':
    nums_ = [0,2,1,5,3,4]
    output = buildArray(None, nums_)
    print(output)
