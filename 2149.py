def main(nums):
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


if __name__ == '__main__':
    _nums = [3, 1, -2, -5, 2, -4]
    main(_nums)
