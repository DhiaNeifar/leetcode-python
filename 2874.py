from typing import List


def maximumTripletValue(self, nums: List[int]) -> int:
    maxprefix, maxdiff = nums[0], 0
    result = 0
    for k in range(1, len(nums)):
        result = max(result, maxdiff * nums[k])
        maxprefix = max(maxprefix, nums[k])
        maxdiff = max(maxdiff, maxprefix - nums[k])
    return result


if __name__ == '__main__':
    nums_ = [8,6,3,13,2,12,19,5,19,6,10,11,9]
    print(maximumTripletValue(None, nums_))
