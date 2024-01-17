def main(nums):
    if len(nums) == 1:
        return [nums]
    _max = -1
    d = {}
    for element in nums:
        if element in d:
            d[element] += 1
        else:
            d[element] = 0
        _max = max(_max, d[element])
    l = [[] for _ in range(_max + 1)]
    for i in range(len(l)):
        for element in d:
            if d[element] >= i:
                l[i].append(element)
    return l


if __name__ == '__main__':
    _nums = [2, 3, 1]
    main(_nums)
