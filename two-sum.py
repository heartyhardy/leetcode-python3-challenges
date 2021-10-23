class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hm:
                return [i, hm[rem]]
            hm[nums[i]] = i