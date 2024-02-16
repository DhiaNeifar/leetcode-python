def main(nums):
    count = 1
    element = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] == element:
            count += 1
        else:
            if count > 1:
                count -= 1
            else:
                element = nums[i]
                count = 1
        i += 1
    return element


if __name__ == '__main__':
    _nums = [3, 2, 3]
    print(main(_nums))
