class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1 
        #get the prefix 
        for i in range(n):
            result[i] = result[i] * prefix
            prefix *= nums[i]
        #o(n)
        suffix = 1
        for i in range(n-1, -1 , -1):
            result[i] = result[i]*suffix
            suffix = nums[i]*suffix
        return result



        