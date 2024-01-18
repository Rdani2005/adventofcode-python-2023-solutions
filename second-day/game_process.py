from game_set import GameSet
from typing import List

class GameProcess:
    def __init__(self, game_sets: List[GameSet] = []):
        self.game_sets: List[GameSet] = game_sets
    
    def process_valid_games(self) -> int:
        return sum(
            map(lambda game_set: game_set.id, filter(lambda game_set: game_set.validate_game(), self.game_sets))
        )
    
    def get_sets_power_total(self) -> int:
        return sum(map(lambda game_set: game_set.multiply_colors(), self.game_sets))
