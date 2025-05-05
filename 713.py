from typing import List

def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k == 0 or (len(nums) < 2 and nums[0] < k):
        return 0
    subarrays = 0
    i = 0
    while i < len(nums):
        j = i + 1
        product = nums[i]
        while j < len(nums) and product < k:
            product *= nums[j]
            j += 1
        subarrays += (j - i - 1) * (j - i) // 2
        i += 1

    return subarrays


if __name__ == '__main__':
    nums_ = [10,5,2,6]
    k_ = 100
    output = numSubarrayProductLessThanK(None, nums_, k_)
    print(output)