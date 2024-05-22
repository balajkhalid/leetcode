# Merge Sorted Array

## Problem

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers m and n, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. `nums2` has a length of n.

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Given two sorted arrays, `nums1` and `nums2`, the task is to merge them into a single sorted array stored in `nums1`. The first m elements of `nums1` and the first n of `nums2` contain valid elements. I leverage the fact that both arrays are already sorted, this simplifies the merging process by allowing us to compare elements from start of the arrays and insert them in the correct order, ensuring we only need linear time to complete the task.

## Approach
<!-- Describe your approach to solving the problem. -->
1. Filter Relevant Elements: Since `nums1` or `nums2` may have some deacreasing elements we filter first m elements for `nums1` and n elements for `nums2`.
2. Initialize Indexes: We use three indexes: i for iterating through the copied part of `nums1` (`nums1_copy`), j for iterating through `nums2`, and k for placing elements in the correct position in the final merged `nums1`.
3. Merge Arrays: We iterate through both arrays `nums1_copy` and `nums2`, comparing elements at indexes i and j. We place the smaller element in the position indicated by k in `nums1` and increment the respective indexes.
4. Handle Remaining Elements: If we run of out bounds for any array the remaining elements of other array placed into `nums1`.

(Link to LeetCode Submission)[https://leetcode.com/problems/merge-sorted-array/solutions/5191924/easy-python-solution]

## Complexity

- Time complexity: $$O(m+n)$$
- Space complexity: $$O(m)$$

## Code
```
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
```