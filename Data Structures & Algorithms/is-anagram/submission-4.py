class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #dict
        # count = {}
        # #someway to have all letters frequency zero
        # for letter in s:
        sSorted = sorted(s)
        tSorted = sorted(t)
        if sSorted == tSorted:
            return True
        else:
            return False

        