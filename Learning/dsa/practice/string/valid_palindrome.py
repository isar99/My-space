# class Solution:
     # TC -> N, SC -> N
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ''
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]


class Solution:
    # TC -> N, SC -> 1
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while r > l:
            while r > l and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    sz = "Was it a car or a cat I saw?"
    sol = Solution()
    print(sol.isPalindrome(sz))



