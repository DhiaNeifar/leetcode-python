def main(nums):
    if len(nums) == 1:
        return True
    max_index, max_ = 0, nums[0]
    for index, num in enumerate(nums):
        if max_ <= num:
            max_ = num
            max_index = index
    for index in range(max_index + 1, max_index + len(nums)):
        if nums[index % len(nums)] > nums[(index + 1) % len(nums)]:
            return False
    return True


if __name__ == '__main__':
    _nums = [1, 2, 3]
    print(main(_nums))
