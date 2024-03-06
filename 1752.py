def main(nums):
    huh = 0
    for i in range(-1, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            huh += 1
    return not huh > 1



if __name__ == '__main__':
    _nums = [3, 4, 5, 1, 2]
    print(main(_nums))
