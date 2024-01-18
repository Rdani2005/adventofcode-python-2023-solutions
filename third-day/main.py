from analizer import Analyzer

with open("data.txt") as file:
    schema = file.read()

analyzer: Analyzer = Analyzer(schema)
total = analyzer.calculate_sum_numbers()
gear_total = analyzer.calculate_sum_of_all_gear_ratios()
print(f"Total part numbers: {total}")
print(f"Total gear: {gear_total}")