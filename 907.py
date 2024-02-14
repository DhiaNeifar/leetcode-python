def main(arr):
    def sum_sub_array_min(_list):
        if len(_list) == 0:
            return 0
        if len(_list) == 1:
            return _list[0]
        pos, _min = 0, _list[0]
        i = 1
        while i < len(_list):
            if _list[i] < _min:
                _min = _list[i]
                pos = i
            i += 1
        return _min * ((pos + 1) * (len(_list) - pos)) + sum_sub_array_min(_list[:pos]) + sum_sub_array_min(_list[pos + 1:])
    return sum_sub_array_min(arr)


if __name__ == '__main__':
    _arr = [3, 1, 2, 4]
    print(main(_arr))
