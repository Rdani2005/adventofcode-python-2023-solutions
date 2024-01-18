from game_record import GameRecord
from typing import List, Dict
class GameSet:
    def __init__(self, id: int, records: List[GameRecord] = []):
        self.id: int = id
        self.records: List[GameRecord] = records

    def validate_game(self) -> bool:
        return all(map(lambda record: record.validate_part_one(), self.records))
    
    def validate_min_required_cubes(self) -> Dict[str, int]:
        return {
            "green": max(map(lambda record: record.green, self.records)),
            "red": max(map(lambda record: record.red, self.records)),
            "blue": max(map(lambda record: record.blue, self.records))
        }
        
    def multiply_colors(self) -> int:
        values: Dict[str, int] = self.validate_min_required_cubes()
        total = values["green"] * values["red"] * values["blue"]
        return total
        