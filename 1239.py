def main(arr):
    scores = []
    sets = []
    for s in arr:
        scores.append(score(s))
        sets.append(set(s))
    for i in range(1, len(arr)):
        max_score = scores[i]
        new_set = sets[i]
        for j in range(i):
            if not sets[i] & sets[j]:
                sets[i] = sets[i] | sets[j]
                max_score = max(max_score, max_score + scores[j])
    return max(scores)


def score(s):
    frequency_dict = {}
    for element in s:
        frequency = frequency_dict.get(element, 0)
        if frequency:
            return 0
        frequency_dict[element] = 1
    return len(s)



if __name__ == '__main__':
    _arr = ["un", "iq", "ue"]
    print(main(_arr))
