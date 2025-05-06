from typing import List

def getAverages(self, nums: List[int], k: int) -> List[int]:
        i = 0
        window = 0
        result = []
        while i < len(nums):
            if i - k < 0 or i + k >= len(nums):
                result.append(-1)
            else:
                if window == 0:
                    for j in range(i - k, i + k + 1):
                        window += nums[j]
                else:
                    window -= nums[i - k - 1]
                    window += nums[i + k]
                print(k)
                print(window)
                print(2 * k + 1)
                print(window // (2 * k + 1))
                result.append(window // (2 * k + 1))
            i += 1
        return result


if __name__ == '__main__':
    nums_ = [100000]
    k_ = 0
    output = getAverages(None, nums_, k_)
    print(output)