class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        #store as {3:0, 4:1, 5:2, 6:3}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in count:
                return [count[want], i]
            count[nums[i]] = i
        