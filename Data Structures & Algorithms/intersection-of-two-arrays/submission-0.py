class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[] #to store the intersected array
        for num in nums2:
            if(num in nums1 and num not in ans):
                ans.append(num)

        return ans
        