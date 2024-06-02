def main(word, ch):
    for index, letter in enumerate(word):
        if letter == ch:
            return word[:index + 1][::-1] + word[index + 1:]
    return word


if __name__ == '__main__':
    _word = "abcdefd"
    _ch = "w"
    main(_word, _ch)
