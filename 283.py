from typing import List


def moveZeroes1(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeros = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1
        else:
            nums[i - zeros] = nums[i]

def moveZeroes(self, nums: List[int]) -> None:
    i = 0
    zeros = 0
    while i + zeros < len(nums):
        if nums[i + zeros] == 0:
            zeros += 1
        else:
            nums[i] = nums[i + zeros]
            i += 1
    while i < len(nums):
        nums[i] = 0
        i += 1

if __name__ == '__main__':
    nums_ = [0,1,0,3,12]
    moveZeroes(None, nums_)
    print(nums_)
