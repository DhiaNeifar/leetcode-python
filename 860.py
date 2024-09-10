def main(bills) -> bool:
    change = {5: 0, 10: 0, }
    for bill in bills:
        if bill == 5:
            change[5] = change[5] + 1
        if bill == 10:
            if not change[5]:
                return False
            change[5] = change[5] - 1
            change[10] = change[10] + 1
        if bill == 20:
            priority = False
            if change[10] > 0 and change[5] > 0:
                priority = True
                change[10] = change[10] - 1
                change[5] = change[5] - 1
            if not priority:
                if change[5] < 3:
                    return False
                change[5] = change[5] - 3
    return True


if __name__ == '__main__':
    bill_ = [5, 5, 5, 10, 5, 20, 5, 10, 5, 20]
    print(main(bill_))
