class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftMostRowIndex = 0
        rightMostRowIndex = len(matrix)-1
        while leftMostRowIndex <= rightMostRowIndex:
            mid = (leftMostRowIndex+rightMostRowIndex)//2
            if target > matrix[mid][-1]:
                leftMostRowIndex = mid+1
            elif target < matrix[mid][0]:
                rightMostRowIndex = mid-1
            else:
                l = 0
                r = len(matrix[mid])-1
                while l<=r:
                    mid1 = (l+r)//2
                    if target > matrix[mid][mid1]:
                        l = mid1+1
                    elif target < matrix[mid][mid1]:
                        r = mid1-1
                    else:
                        return True
                return False
        return False

            