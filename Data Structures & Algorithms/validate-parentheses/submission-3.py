class Solution:
    def isValid(self, s: str) -> bool:
        #create a dictionary to map items
        pairs = {
            ")":"(", 
            "]":"[",
            "}":"{"
        }
        #In Python, a list can act as a stack:
        stack = []
        for char in s:
            if char in pairs.values():
                stack.append(char) #["["]
                print(stack)
            #now if its a closing one
            else:
                if not stack:
                    return False
                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
        