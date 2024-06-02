from math import floor


def main(img):
    n, m = len(img), len(img[0])
    new_img = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            avg = 0
            count = 0
            for x in range(max(0, i - 1), min(n, i + 2)):
                for y in range(max(0, j - 1), min(m, j + 2)):
                    count += 1
                    avg += img[x][y]
            new_img[i][j] = floor(avg / count)
    return new_img


if __name__ == '__main__':
    img_ = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    main(img_)

