from typing import List

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    longest_sequence = 0
    left, right = 0, 0
    num_zeros = 0

    while right < len(nums):
        if nums[right] == 0:
            num_zeros += 1

        while num_zeros == 2:
            if nums[left] == 0:
                num_zeros += 1
            left += 1
        print(f"left: {left}, right: {right}")
        longest_sequence = max(longest_sequence, right - left + 1)
        right += 1

    return longest_sequence


if __name__ == '__main__':
    nums_ = [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0]
    output = findMaxConsecutiveOnes(None, nums_)
    print(output)