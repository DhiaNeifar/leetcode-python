def lengthOfLongestSubstring(self, s: str) -> int:
    seen = [0 for _ in range(256)]
    last_seen = [0 for _ in range(256)]
    result = 0
    for ind, char in enumerate(s):
        index = ord(char)
        if seen[index]:
            result = max(result, ind - last_seen[index])
        seen[index] = 1
        last_seen[index] = ind
    return result

if __name__ == '__main__':
    s_ = "abcabcbb"
    output = lengthOfLongestSubstring(None, s_)
    print(output)