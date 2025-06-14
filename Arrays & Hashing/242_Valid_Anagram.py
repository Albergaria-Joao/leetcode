class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}

        for char in s:
            chars[char] = chars.get(char, 0) + 1 

        for char in t:
            chars[char] = chars.get(char, 0) - 1 

        for char in chars:
            if chars[char] != 0:
                return False

        return True
