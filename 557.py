def main(s):
    return ' '.join([word[::-1] for word in s.split(' ')])


if __name__ == '__main__':
    _s = "Let's take LeetCode contest"
    print(main(_s))
