class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        i = 0
        j = len(s) - 1 

        while i < j:
            if not self.isAlphabet(s[i]):
                i+=1
                continue
            if not self.isAlphabet(s[j]):
                j-=1
                continue

            print(f"DEBUG i:{i}, j: {j}, s[i]: {s[i]}, s[j]: {s[j]}")
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else:
                return False

        return True
    def isAlphabet(self, c):
        val = ord(c.lower())
        if val < 123 and val > 96:
            return True
        if val < 58 and val > 47:
            return True
        return False

        