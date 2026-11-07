# class Solution:
#     # TC -> N, SC -> 1
#     def search(self, nums, target: int) -> int:
#         if target not in nums:
#             return -1
#         return nums.index(target)

# class Solution:
#     # TC -> logN, SC -> logN
#     def bs(self, left, right, nums, target):
#         if left > right:
#             return -1
#         mid = left + (right - left)//2
#
#         if nums[mid] == target:
#             return mid
#         if nums[mid] < target:
#             return self.bs(mid+1, right, nums, target)
#         return self.bs(0, mid - 1, nums, target)
#
#     def search(self, nums, target: int) -> int:
#         return self.bs(0, len(nums) - 1, nums, target)

class Solution:
    # TC -> logN, SC -> logN
    def search(self, nums, target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] < target:
                l=m+1
            elif nums[m] > target:
                r=m-1
            else:
                return m
        return -1


if __name__ == "__main__":
    x = [-2, 0, 6, 7, 9]
    target = 7
    sol = Solution()
    print(sol.search(x, target))