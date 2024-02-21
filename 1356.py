def main(arr):
    return sorted(arr, key=lambda x: (x.bit_length(), x.bit_count()))


if __name__ == '__main__':
    _arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    print(main(_arr))
