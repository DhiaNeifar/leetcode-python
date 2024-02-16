def main(words):
    def is_palindrome(string):
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
    index = 0
    while index < len(words):
        if is_palindrome(words[index]):
            return words[index]
        index += 1
    return ''


if __name__ == '__main__':
    _words = ["def", "ghi"]
    main(_words)
