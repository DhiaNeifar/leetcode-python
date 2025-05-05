from typing import List

def replaceElements(self, arr: List[int]) -> List[int]:
    curr_max = -1
    placeholder = arr[-1]
    arr[-1] = -1
    for i in range(len(arr) - 2, -1, -1):
        curr_max = max(curr_max, placeholder)
        placeholder = arr[i]
        arr[i] = curr_max
    return arr


if __name__ == '__main__':
    arr_ = [17, 18, 5, 4, 6, 1]
    output = replaceElements(None, arr_)
    print(output)
