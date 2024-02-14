def main1(nums):
    # Basic 2 loops
    positive, negative = [], []
    for num in nums:
        if num > 0:
            positive.append(num)
        else:
            negative.append(num)
    i = 0
    results = []
    while i < len(positive):
        results.append(positive[i])
        results.append(negative[i])
        i += 1
    return results


def main(nums):
    # 1 loop
    results = []
    i, j = 0, 0
    while i < len(nums) and j < len(nums):
        while nums[i] < 0:
            i += 1
        while nums[j] > 0:
            j += 1
        results.append(nums[i])
        results.append(nums[j])
        i += 1
        j += 1
    return results

if __name__ == '__main__':
    _nums = [3, 1, -2, -5, 2, -4]
    main(_nums)
