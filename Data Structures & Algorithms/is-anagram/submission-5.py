class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = {}
        for char in s:
            chars_s[char] = chars_s.get(char, 0) + 1
        
        chars_t = {}
        for char in t:
            chars_t[char] = chars_t.get(char, 0) + 1

        if chars_s.items() != chars_t.items():
            return False
            
        for key, value in chars_s.items():
            if chars_t.get(key, 0) != value:
                return False
        return True

        