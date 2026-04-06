class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Given array nums
        # Return true if value appears more than once

        # Sorting approach, set approach
        # Sorting takes more time, set takes more space

        # Sorting Approach
        # sorted_nums = sorted(nums)
        # for i in range(1, len(sorted_nums)):
        #     if sorted_nums[i] == sorted_nums[i - 1]:
        #         return True
        # return False

        # Set Approach
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
