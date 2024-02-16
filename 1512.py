def main(nums):
    freq = {}
    count = 0
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for num in freq:
        n = freq[num]
        count += n * (n - 1) // 2
    return count


if __name__ == '__main__':
    _nums = []
    main(_nums)
