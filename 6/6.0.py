import sys

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = []

        for _ in range(0, numRows):
            rows.append([])

        currentRow = 0
        zigzagAscending = True
        
        for char in s:
            rows[currentRow].append(char)

            if zigzagAscending:
                if currentRow == numRows - 1:
                    zigzagAscending = False
                    currentRow = currentRow - 1 if numRows > 1 else 0
                else:
                    currentRow += 1
            else:
                if currentRow == 0:
                    zigzagAscending = True
                    currentRow = currentRow + 1 if numRows > 1 else 0
                else:
                    currentRow -= 1

        result = ""

        for index in range(0, numRows):
            result += "".join(rows[index])
        
        return result

print((Solution()).convert("PAYPALISHIRING", 1))
