def main(arr):
    # Execution Time Exceeded
    constant = 10 ** 9 + 7
    count = 0
    for i in range(len(arr)):
        i_min, i_max = i, i
        while i_min - 1 >= 0 and arr[i_min - 1] > arr[i]:
            i_min -= 1
        while i_max + 1 <= len(arr) - 1 and arr[i_max + 1] >= arr[i]:
            i_max += 1
        count += arr[i] * (i - i_min + 1) * (i_max - i + 1)
    return count % constant


if __name__ == '__main__':
    _arr = [71, 55, 82, 55]
    print(main(_arr))
