def main1(nums, k):
    # Time Limit exceeded
    n = len(nums)
    for i in range(n - 1, 0, -1):
        nums[i], nums[i - k - 1] = nums[i - k - 1], nums[i]
    print(nums)
    pass


def main(nums, k):
    n = len(nums)
    for i in range(n // 2):
        nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
    print(nums)
    # inverse first list
    for i in range(k // 2):
        nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
    print(nums)
    # inverse second list
    for i in range((n - k) // 2):
        nums[n - k - 1 + i], nums[n - i - 1] = nums[n - i - 1], nums[n - k - 1 + i]
    print(nums)
    pass


def rotate(self, nums, k: int) -> None:
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n  # In case k is larger than n
    # Helper function to reverse a portion of the array

    # Reverse the entire array
    reverse(0, n - 1)
    # Reverse the first k elements
    reverse(0, k - 1)
    # Reverse the remaining n - k elements
    reverse(k, n - 1)


if __name__ == '__main__':
    nums_ = [1, 2, 3, 4, 5, 6, 7]
    k_ = 3
    main(nums_, k_)
