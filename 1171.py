def main(head):
    i = 0
    while i < len(head):
        sum_ = head[i]
        j = i + 1
        while j < len(head) and sum_ + head[j]:
            sum_ += head[j]
            j += 1
        if j == len(head):
            return head[i:]
        else:
            i = j + 1


if __name__ == '__main__':
    head_ = [1,2,3,-3,4]
    print(main(head_))
