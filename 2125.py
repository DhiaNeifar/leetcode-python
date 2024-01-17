def main(bank):
    def count_devices(_row):
        _count = 0
        for binary in _row:
            if binary == '1':
                _count += 1
        return _count

    devices_count = []
    for row in bank:
        devices = count_devices(row)
        if devices:
            devices_count.append(devices)

    if len(devices_count) == 1:
        return 0

    count = 0
    for i in range(1, len(devices_count)):
        count += devices_count[i] * devices_count[i - 1]
    return count


if __name__ == '__main__':
    _bank = ["011001", "000000", "010100", "001000"]
    main(_bank)
