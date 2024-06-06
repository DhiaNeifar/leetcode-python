def main(nums):
    parity = nums[0] & 1
    for i in range(1, len(nums)):
        new_parity = nums[i] & 1
        if new_parity == parity:
            return False
        parity = new_parity
    return True


if __name__ == '__main__':
    nums_ = [4, 3, 2, 1, 6]
    print(main(nums_))
