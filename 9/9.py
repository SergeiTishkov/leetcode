class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False

        digits = []
        while (x > 9):
            digits.append(x % 10)
            x = int(x / 10)
        
        digits.append(x)

        digits_number = len(digits)
        middle = digits_number / 2

        left, right = 0, 0
        if (middle % 1 == 0):
            middle = int(middle)
            left, right = middle - 1, middle
        else:
            middle = int(middle)
            left, right = middle - 1, middle + 1

        while left >= 0 and right < digits_number:
            if digits[left] != digits[right]:
                return False

            left -= 1
            right += 1

        return True