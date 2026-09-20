class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map={}
        n = len(s)
        for i in range (0,n):
            hash_map[s[i]] = hash_map.get(s[i],0)+1
        for i in range (0,n):
            if hash_map[s[i]] == 1:
                return i

        return -1