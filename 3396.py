from typing import List


def minimumOperations1(self, nums: List[int]) -> int:
    def check_notdistinct(dictionary):
        for element in dictionary.values():
            if element > 1:
                return True
        return False

    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    operations = 0
    while freq_dict and check_notdistinct(freq_dict):
        for element in range(operations * 3, min(len(nums), (operations + 1) * 3)):
            freq_dict[nums[element]] -= 1
            if freq_dict[nums[element]] == 0:
                freq_dict.pop(nums[element])
        operations += 1
    return operations


def minimumOperations(self, nums: List[int]) -> int:
    x, y = len(nums) % 3, len(nums) // 3
    our_set = set()
    if x == 1:
        our_set.add(nums[-1])
    if x == 2:
        our_set.add(nums[-1])
        if nums[-2] in our_set:
            return y + 1
        our_set.add(nums[-2])
    while y:
        for j in range(y * 3 - 1, (y - 1) * 3 - 1, -1):
            if nums[j] in our_set:
                return y
            else:
                our_set.add(nums[j])
        y -= 1
    return 0


if __name__ == '__main__':
    dict_ = [1, 2, 3, 4, 2, 3, 3, 5, 7, 8, 9]
    print(minimumOperations(None, dict_))
