class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        string_char_index = 0

        for index in range(len(pattern)):
            if pattern[index] != string[index]:
                return False
        
        return True
                

def check(expected, actual):
    if (expected != actual):
        raise ValueError("Expected: " + str(expected) +"; Actual: " + str(actual))

sol = Solution()

check(sol.isMatch("aa", "a"), False)
check(sol.isMatch("aa", "a*"), True)
check(sol.isMatch("ab", ".*"), True)
check(sol.isMatch("aab", "c*a*b"), True)
check(sol.isMatch("mississippi", "mis*is*p*."), False)