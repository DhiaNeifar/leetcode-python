def main(intervals):
    ans = []
    intervals.sort(key=lambda x: x[0])
    for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])
    return ans


if __name__ == '__main__':
    _intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    main(_intervals)
