class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # first try
        # it have unnessiary memory space and copy, more faster and reverse compare two value, and merge list 
        # p1=0
        # p2=0
        # p=0
        # back_nums1=nums1[:m]
        # back_nums2=nums2[:n]
        # while p1 < m and p2<n:
        #     if back_nums1[p1] >= back_nums2[p2]:
        #         nums1[p]=back_nums2[p2]
        #         p2+=1
        #         p+=1

        #     else:
        #         nums1[p]=back_nums1[p1]
        #         p1+=1
        #         p+=1


        # if p < m+n :
        #     if p1 < m:
        #         while p1 < m:
        #             nums1[p]=back_nums1[p1]
        #             p1+=1
        #     else:
        #         while p2 <n:
        #             nums1[p]=back_nums2[p2]
        #             p2+=1
        #             p+=1
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
            
   
        
