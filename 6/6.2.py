import sys

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        distances = [None] * numRows
        distances[0] = [(numRows - 1) * 2]
        distances[numRows - 1] = [(numRows - 1) * 2]

        first_distance = distances[0][0] - 2
        second_distance = 2

        for i in range(1, numRows - 1):
            distances[i] = [first_distance, second_distance]
            first_distance -= 2
            second_distance += 2

        s_length = len(s)
        result_list = [None] * s_length
        current_index = 0

        starting_char = 0

        for distance_range in distances:
            current_char_number = starting_char

            while current_char_number < s_length:
                for distance in distance_range:
                    if current_char_number < s_length:
                        result_list[current_index] = s[current_char_number]
                        current_index += 1

                    if current_char_number + distance < s_length:
                        current_char_number += distance
                    else:
                        current_char_number = s_length
            
            starting_char += 1

        return str.join("", result_list)



print((Solution()).convert("PAYPALISHIRING", 3))
