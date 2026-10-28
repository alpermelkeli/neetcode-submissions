class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = self.buildMap(s)
        tMap = self.buildMap(t)
        
        if len(sMap) != len(tMap):
            return False 

        for key in sMap:
            if ((key in tMap) and (sMap[key] == tMap[key])):
                continue
            else:
                return False
        return True

    def buildMap(self, s: str) -> dict():
        hashMap = dict()
        for char in s: 
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1
        return hashMap 