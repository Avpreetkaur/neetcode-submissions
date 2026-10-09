class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #get the product beforehand ]
        result = []
        mult = 1
        zero_count = 0
        #get the product without zero
        for num in nums:
            if num==0:
                zero_count += 1
            else: 
                mult *= num
        
        if zero_count > 1:
            return [0]*len(nums)
        
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    result.append(mult)
                else:
                    result.append(0)
            else:
                result.append(mult//num)
        return result

        