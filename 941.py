from typing import List

def validMountainArray(self, arr: List[int]) -> bool:
    if len(arr) < 3:
        return False
    i = 0
    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1
    if i == len(arr) - 1 or i == 0:
        return False
    while i < len(arr) - 1 and arr[i] > arr[i + 1]:
        i += 1
    return i == len(arr) - 1

if __name__ == '__main__':
    arr_ = [0,1,2,3,4,5,6,7,8,9]
    output = validMountainArray(None, arr_)
    print(output)