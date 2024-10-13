class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
            subarrays=[]            
            for i in range(0,len(nums)-k+1):
                subarray=nums[i:i+k]
                freq = Counter(subarray)
                most_common = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))[:x]             
                subarrays.append(sum(key*val for key,val in most_common))
            return subarrays