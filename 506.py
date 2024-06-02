def main(score):
    scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

    results = ['' for _ in range(len(scores))]
    for index, score in enumerate(scores):
        if index == 0:
            results[score[0]] = "Gold Medal"
        elif index == 1:
            results[score[0]] = "Silver Medal"
        elif index == 2:
            results[score[0]] = "Bronze Medal"
        else:
            results[score[0]] = str(index + 1)
    return results


if __name__ == '__main__':
    score_ = [10, 3, 8, 9, 4]
    main(score_)
