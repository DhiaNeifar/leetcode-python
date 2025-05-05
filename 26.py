from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    i, j = 1, 1
    while j < len(nums) - 1:
        k = j + 1
        while k < len(nums) and nums[k] == nums[j]:
            k += 1
        if k < len(nums):
            nums[i] = nums[k]
            i += 1
        j = k
    return i


if __name__ == '__main__':
    nums_ = [0,0,1,1,1,2,2,3,3,4]
    output = removeDuplicates(None, nums_)
    print(output)
