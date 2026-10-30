class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        istart = 0
        longest = 0
        j = 1

        while j < len(s):

            for i in range(istart, j):
                if s[j] == s[i]:
                    istart = i + 1
                    break

            longest = max(j - istart + 1, longest)
            j += 1

        return longest
        