from typing import List


def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    for domino in dominoes:
        if domino[1] < domino[0]:
            domino[0], domino[1] = domino[1], domino[0]
    dominoes.sort(key=lambda x: x[1])
    dominoes.sort(key=lambda x: x[0])
    print(dominoes)
    equivalent = 0
    i = 0
    while i < len(dominoes) - 1:
        j = i + 1
        while j < len(dominoes) and dominoes[i] == dominoes[j]:
            j += 1
        n = j - i

        equivalent += n * (n - 1) // 2
        i = j
    return equivalent


if __name__ == '__main__':
    dominoes_ = [[1, 1], [2, 2], [1, 1], [1, 2], [1, 2], [1, 1]]
    output = numEquivDominoPairs(None, dominoes_)
    print(output)
