class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        nums1_pointer, nums2_pointer = 0, 0
        merged_list = []
        while nums1_pointer < m or nums2_pointer < n:
            if nums1_pointer == m:
                merged_list = merged_list + nums2[nums2_pointer:]
                break
            if nums2_pointer == n:
                merged_list = merged_list + nums1[nums1_pointer:]
                break
            if nums1[nums1_pointer] <= nums2[nums2_pointer]:
                merged_list.append(nums1[nums1_pointer])
                nums1_pointer += 1
            else:
                merged_list.append(nums2[nums2_pointer])
                nums2_pointer += 1
        if len(merged_list)%2 == 1:
            return merged_list[len(merged_list)//2]
        else:
            return (merged_list[len(merged_list)//2]+merged_list[len(merged_list)//2-1])/2