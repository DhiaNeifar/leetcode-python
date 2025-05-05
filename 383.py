def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    ransomDict, magazineDict = {}, {}
    for char in ransomNote:
        ransomDict[char] = ransomDict.get(char, 0) + 1
    for char in magazine:
        magazineDict[char] = magazineDict.get(char, 0) + 1
    for char in ransomDict:
        if ransomDict[char] > magazineDict.get(char, 0):
            return False
    return True


if __name__ == '__main__':
    ransomNote_ = "aa"
    magazine_ = "aab"
    output = canConstruct(None, ransomNote_, magazine_)
    print(output)
