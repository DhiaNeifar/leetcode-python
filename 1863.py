from typing import List


def subsetXORSum(self, nums: List[int]) -> int:
    XORList = [0]
    total_sum = 0
    for num in nums:
        XORListLength = len(XORList)
        for i in range(XORListLength):
            xor_result = XORList[i] ^ num
            total_sum += xor_result
            XORList.append(xor_result)
    return total_sum


if __name__ == '__main__':
    nums_ = [3,4,5,6,7,8]
    output = subsetXORSum(None, nums_)
    print(output)
