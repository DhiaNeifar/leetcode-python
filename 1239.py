def main(arr):
    _list = [len(arr[i]) if len(arr[i]) == len(set(arr[i])) else 0 for i in range(len(arr))]
    if len(_list) == 1:
        return _list[-1]
    curr_string = arr[-1]
    _max = _list[-1]
    for i in range(len(arr) - 2, -1, -1):
        new_string = ''.join([arr[i], curr_string])
        if len(new_string) == len(set(new_string)):
            curr_string
    pass


if __name__ == '__main__':
    _arr = ["un", "iq", "ue"]
    main(_arr)
