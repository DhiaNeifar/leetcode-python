def main(nums):
    def count_operations(x):
        n = 0
        while (x + n) % 3 != 0:
            n += 1
        return (x + n) // 3
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    operations = 0
    for value in count.values():
        if value == 1:
            return -1
        operations += count_operations(value)
    return operations


if __name__ == '__main__':
    _nums = [14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]
    print(main(_nums))
