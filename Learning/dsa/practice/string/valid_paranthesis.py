# class Solution:
#     def isValid(self, s: str) -> bool:
#         # TC -> N, SC -> 1
#         accepted_chars_in_s = ["(", ")", "{", "}", "[", "]"]
#         closing_chars = {"(":")", "{":"}", "[":"]", ")":"(", "}":"{", "]":"[" }
#         i = 0
#         j = len(s) - 1
#         while i < j:
#             if s[i] not in accepted_chars_in_s:
#                 return False
#             if s[i] != closing_chars[s[j]]:
#                 return False
#             i += 1
#             j -= 1
#         return True

class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i in hash_map:
                if stack and stack[-1] == hash_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return stack == []


if __name__ == "__main__":
    sx = "{()[{]}}"
    sol = Solution()
    print(sol.isValid(sx))