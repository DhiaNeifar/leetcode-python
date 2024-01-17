def main(nums, k):

    # Easy method
    # nums.sort(reverse=True)
    # return nums[k - 1]

    # Complicated
    _max = nums[0]
    for num in nums[1:]:
        if _max < num:
            _max = num
    if k == 1:
        return _max
    _list = []
    while len(_list) < k:
        new_max = -10000
        count = 1
        for num in nums:
            if num < _max:
                if new_max == num:
                    count += 1
                if new_max < num:
                    new_max = num
                    count = 1
        for _ in range(count):
            _list.append(new_max)
    return _list[-1]


if __name__ == '__main__':
    _nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    _k = 4
    print(main(_nums, _k))

