
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]  # 범위 시작점 설정

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:  # 연속되지 않는 경우
                if start == nums[i - 1]:  
                    result.append(str(start))  # 단일 값
                else:
                    result.append(f"{start}->{nums[i - 1]}")  # 범위 추가
                
                start = nums[i]  # 새로운 범위 시작

        # 마지막 범위 처리
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result