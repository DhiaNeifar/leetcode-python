def main(nums):
    if len(nums) == 2:
        return (nums[0] - 1) * (nums[1] - 1)
    _max, _index = 0, -1
    for i, num in enumerate(nums):
        if num > _max:
            _max = num
            _index = i
    __max = 0
    for i, num in enumerate(nums):
        if num > __max and i != _index:
            __max = num
    return (_max - 1) * (__max - 1)


if __name__ == '__main__':
    _nums = [10,2,5,2]
    print(main(_nums))
