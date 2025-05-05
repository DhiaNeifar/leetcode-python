from typing import List

def findMaxAverage(self, nums: List[int], k: int) -> float:
    window = 0
    for i in range(k):
        window += nums[i]
    result = window
    for i in range(1, len(nums) - k + 1):
        window -= nums[i - 1]
        window += nums[i + k - 1]
        result = max(result, window)
    return result / k


if __name__ == '__main__':
    nums_ = [0, 1, 1, 3, 3]
    k_ = 4
    output = findMaxAverage(None, nums_, k_)
    print(output)