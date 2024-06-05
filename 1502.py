def main(arr):
    arr.sort()
    progress = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != progress:
            return False
    return True


if __name__ == '__main__':
    arr_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(main(arr_))
    