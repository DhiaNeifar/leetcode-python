from typing import List

def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
    def from_str_to_integer(string: str) -> int:
        integer_result = 0
        index = 0
        while index < len(string):
            int_ = ord(string[index]) - ord('0')
            if int_ > limit:
                return -1
            integer_result *= 10
            integer_result += int_
            index += 1
        return integer_result
    def check_digits(_solution, _limit):
        while _solution:
            _solution, r = divmod(_solution, 10)
            if r > limit:
                return False
        return True
    solution = 0
    ind = 0
    power = len(s)
    first_trial = 10 ** power
    integer =  from_str_to_integer(s)
    if integer == - 1:
        return solution
    while integer <= finish:
        v = check_digits(ind, limit)
        if integer >= start and v:
            solution += 1
        ind += 1
        integer += first_trial
    return solution


if __name__ == '__main__':
    start_ = 20
    finish_ = 1159
    limit_ = 5
    s_ = "20"
    output = numberOfPowerfulInt(None, start_, finish_, limit_, s_)
    print(output)
