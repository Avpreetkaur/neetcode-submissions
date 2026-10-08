class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        heap = []
        for num in count:
            freq = count[num]
            heap.append((freq,num))
            last = len(heap)-1
            while last > 0:
                parent = (last-1)//2
                if heap[parent][0]<=heap[last][0]:
                    break
                heap[last],heap[parent] = heap[parent], heap[last]

                last = parent #to see more levels up
            
            if len(heap) > k:
                heap[0] = heap[-1]
                heap.pop()
                i = 0 
                while True:
                    min_index = i
                    left_child = 2*i+1
                    right_child = 2*i+2

                    if left_child < len(heap) and heap[left_child][0] < heap[min_index][0]:
                        min_index = left_child
                    if right_child < len(heap) and heap[right_child][0] < heap[min_index][0]:
                        min_index = right_child
                    if i != min_index:
                        heap[min_index],heap[i]=heap[i],heap[min_index]
                        i = min_index
                    else:
                        break
        result = []
        for frequency, num in heap:
            result.append(num)
        return result

            
