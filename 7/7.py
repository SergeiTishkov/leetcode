class Solution:
    def reverse(self, x: int) -> int:
        x_reversed =  int(str(abs(x))[::-1])

        if x < 0:
            x_reversed *= -1
        
        if x_reversed > 2147483647 or x_reversed < -2147483648:
            return 0
        else:
            return x_reversed