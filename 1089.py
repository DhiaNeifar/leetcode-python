from typing import List

def duplicateZeros1(self, arr: List[int]) -> None:
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            for j in range(len(arr) - 2, i - 1, -1):
                arr[j + 1] = arr[j]
            i += 1
        i += 1


def duplicateZeros(self, arr: List[int]) -> None:
        zeros = 0
        for num in arr:
            if num == 0:
                zeros += 1

        i = len(arr) - 1
        while i > -1:
            if i + zeros < len(arr):
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < len(arr):
                    arr[i + zeros] = 0
            i -= 1


if __name__ == '__main__':
    arr_ = [0,4,1,0,0,8,0,0,3]
    duplicateZeros(None, arr_)
    print(arr_)
