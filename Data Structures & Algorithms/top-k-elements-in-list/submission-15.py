class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        #create a buckets list
        buckets = [ [] for _ in range(len(nums)+1) ]
        #dd frequencies to the bucket
        for num in count:
            freq = count[num]
            buckets[freq].append(num)
        
        #collect the values 
        result = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                
                if len(result)==k:
                    return result
