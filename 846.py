def main(hand, groupSize):
    if len(hand) % groupSize:
        return False
    hand.sort()
    num_boxes = len(hand) // groupSize
    results = [[] for _ in range(num_boxes)]
    i = 0
    while i < len(hand):
        j = i
        while j < len(hand) and hand[i] == hand[j]:
            k, not_added = 0, 1
            while k < num_boxes:
                if not len(results[k]) or (results[k][-1] + 1 == hand[j] and len(results[k]) < groupSize):
                    results[k].append(hand[i])
                    not_added = 0
                    break
                k += 1
            if not_added:
                return False
            j += 1
        i = j
    return True


if __name__ == '__main__':
    hand_ = [1, 2, 3, 3, 4, 4, 5, 6]
    groupSize_ = 4
    print(main(hand_, groupSize_))
