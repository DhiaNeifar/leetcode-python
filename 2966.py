def main(nums, k):
    nums.sort()
    results = [[] for _ in range(len(nums) // 3)]
    for i in range(len(nums)):
        results[i // 3].append(nums[i])
    for section in results:
        if section[2] - section[1] > k or section[1] - section[0] > k or section[2] - section[0] > k:
            return []
    return results


if __name__ == '__main__':
    nums_ = [15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2]
    k_ = 2
    print(main(nums_, k_))
