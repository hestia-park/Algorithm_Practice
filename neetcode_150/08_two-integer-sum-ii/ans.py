class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left,right=0,len(numbers)-1
        # while left<right:
        #     current_sum = numbers[left] + numbers[right]
        #     if current_sum == target:
        #         return [left + 1, right + 1] 
        #     elif current_sum < target:
        #         left += 1  
        #     else:
        #         right -= 1  
        # return ans
        def binary_search(left: int, right: int, x: int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == x:
                    return mid
                elif numbers[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        for i in range(len(numbers)):
            complement = target - numbers[i]
            j = binary_search(i + 1, len(numbers) - 1, complement)
            if j != -1:
                return [i + 1, j + 1] 
