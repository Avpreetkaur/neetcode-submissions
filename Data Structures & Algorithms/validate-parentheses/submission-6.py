class Solution:
    def isValid(self, s: str) -> bool:
        #create a dic to map
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        #loop through characters and see if char in pair's values 
        for char in s:
            if char in "([{":
                stack.append(char) #"["("]
            else:
                if not stack:
                    return False
                if pairs[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
