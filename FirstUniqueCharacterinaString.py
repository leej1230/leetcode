class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        ind = {}
        for i,ch in enumerate(s):
            d[ch] = d.get(ch, 0) + 1
            if ch not in ind:
                ind[ch] = i
                
        for key, val in d.items():
            if val == 1:
                return ind[key]
        
        return -1