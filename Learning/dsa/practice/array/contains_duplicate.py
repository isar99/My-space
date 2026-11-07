# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in nums:
#             if i in nums[i:]:
#                 return True
#         return False


class Solution:
    def hasDuplicate(self, nums) -> bool:
        return len(set(nums)) < len(nums)

if __name__ == "__main__":
    ls = [2,4,6]
    sol = Solution()
    print(sol.hasDuplicate(ls))
