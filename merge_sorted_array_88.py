class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        nums2 = nums2[:n]

        i, j, k = 0, 0, 0
        while (k < (m+n)):
            if i < m and j < n:
                if nums1_copy[i] >= nums2[j]:
                    nums1[k] = nums2[j]
                    j = j + 1
                else:
                    nums1[k] = nums1_copy[i]
                    i = i + 1
            elif i >= m and j < n:
                nums1[k] = nums2[j]
                j = j + 1
            elif i < m and j >= n:
                nums1[k] = nums1_copy[i]
                i = i + 1
            k = k + 1