class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the nums 
        nums.sort()
        result = []
        #fix one number
        print(nums)
        for i in range(len(nums)-2):
            print(" i is=" + str(i))
            print("ith number is" + str(nums[i]))
            #skipping duplicate numbers
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total > 0:
                    r-=1
                elif total < 0:
                    l+=1
                else: # found triplet
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                    
        return result
        