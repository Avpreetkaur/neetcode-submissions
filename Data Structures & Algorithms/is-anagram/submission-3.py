class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #0. check the length of both - if thats not same its not
        if len(s) != len(t):
            return False
        #1. create a dict to store character and its frequency
        count = {} 
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]]+=1
            else:
                count[s[i]] = 1
        for j in range(len(t)):
            if t[j] not in count:
                return False
            else:
                count[t[j]]-=1
        for value in count.values():
            if value != 0:
                return False
        return True

        
        