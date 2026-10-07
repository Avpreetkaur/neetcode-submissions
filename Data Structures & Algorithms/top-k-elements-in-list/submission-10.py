class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        sorted_by_freq = sorted(count, key = count.get, reverse=True)
        #how do you sort a dictionary?
        print(sorted_by_freq)
        return sorted_by_freq[:k]