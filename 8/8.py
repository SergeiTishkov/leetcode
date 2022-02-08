class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        read_index_start = 0
        sign = "+"

        for c in s:
            if c == " ":
                read_index_start += 1
            else:
                break

        if read_index_start >= len(s):
            return 0

        if s[read_index_start] == "+" or s[read_index_start] == "-":
            sign = s[read_index_start]
            read_index_start += 1
        elif s[read_index_start] != "+" and s[read_index_start] != "-" and not s[read_index_start].isdigit():
            return 0

        read_end_index = read_index_start

        if read_index_start >= len(s):
            return 0

        for i in range(read_index_start, len(s)):
            if not s[i].isdigit():
                if read_end_index == read_index_start:
                    return 0
                else:
                    read_end_index = i
                    break
            
            read_end_index += 1

        s_result = s[read_index_start:read_end_index]

        result = int(s_result)

        if sign == "-":
            result *= -1

        if result < -2147483648:
            return -2147483648
        elif result > 2147483647:
            return 2147483647
        else:
            return result

print(Solution.myAtoi(None, "42"))
print(Solution.myAtoi(None, "   -42"))
print(Solution.myAtoi(None, "3.14159"))
print(Solution.myAtoi(None, "+"))
print(Solution.myAtoi(None, " "))
