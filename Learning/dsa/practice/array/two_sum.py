class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    # TC -> n^2, SC -> n

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             diff = target - nums[i]
#             if (diff) in nums[i:]:
#                 return [i, nums.index(diff)]
#         return []

if __name__ == "__main__":
    ls = [4,3,6,5]
    target = 8
    sol = Solution()
    print(sol.twoSum(ls,target))