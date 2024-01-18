DIRECTIONS: list = [
    (-1, -1),   # TOP LEFT
    (-1, 0),    # TOP
    (-1, 1),    # TOP RIGHT
    (0, -1),    # CENTER LEFT
    (0, 1),     # CENTER RIGHT
    (1, -1),    # BOTTOM LEFT
    (1, 0),     # BOTTOM
    (1, 1),     # BOTTOM RIGHT
]
class Analyzer:
    def __init__(self, schema) -> None:
        self.schema: list[list] = [list(row) for row in schema.split("\n")]
        self.processed: set = set()

    def valid_symbol(self, char) -> bool:
        return not (char.isdigit() or char == '.')
    
    def valid_number(self, row, col) -> bool:
        for dx, dy in DIRECTIONS:
            if 0 <= row + dx < len(self.schema) and 0 <= col + dy < len(self.schema[row + dx]):
                if self.valid_symbol(self.schema[row + dx][col + dy]):
                    return True

        return False
    
    def _get_gear_ratio(self, row, col):
        adjacent_numbers = []
        for dx, dy in DIRECTIONS:
            adjacent_row, adjacent_col = row + dx, col + dy
            if 0 <= adjacent_row < len(self.schema) and 0 <= adjacent_col < len(self.schema[adjacent_row]):
                if self.schema[adjacent_row][adjacent_col].isdigit():
                    part_number = self._get_full_part_number(adjacent_row, adjacent_col)
                    if part_number not in adjacent_numbers:
                        adjacent_numbers.append(part_number)

        if len(adjacent_numbers) == 2:
            return adjacent_numbers[0] * adjacent_numbers[1]
        return 0

    def calculate_sum_of_all_gear_ratios(self):
        total_sum = 0
        for i, row in enumerate(self.schema):
            for j, char in enumerate(row):
                total_sum += self._get_gear_ratio(i, j) if char == '*' else 0
        
        return total_sum
        
    def calculate_sum_numbers(self) -> int:
        result: int = 0
        for i, row in enumerate(self.schema):
            j = 0
            while j < len(row):
                if row[j].isdigit() and (i, j) not in self.processed:
                    number, init_j = row[j], j
                    while j + 1 < len(row) and row[j + 1].isdigit():
                        number += row[j + 1]
                        j += 1
                    for col_index in range(init_j, j + 1):
                        self.processed.add((i, col_index))
                        if self.valid_number(i, col_index):
                            result += int(number)
                            break
                j += 1
        
        return result 
    
    def _get_full_part_number(self, row, col) -> int:
        # start with the digit at (row, col)
        number_str = self.schema[row][col]

        # fan out to the left
        left_col = col - 1
        while left_col >= 0 and self.schema[row][left_col].isdigit():
            number_str = self.schema[row][left_col] + number_str
            left_col -= 1

        # fan out to the right
        right_col = col + 1
        while right_col < len(self.schema[row]) and self.schema[row][right_col].isdigit():
            number_str += self.schema[row][right_col]
            right_col += 1

        return int(number_str)