from game_process import GameProcess
from game_set import GameSet
from game_record import GameRecord

import re
from typing import List
import time

start_time = time.time()

def get_game_id(entrada) -> int:
    patron = re.compile(r'Game (\d+):')
    coincidencias = patron.findall(entrada)

    if coincidencias:
        return int(coincidencias[0])
    else:
        return None
    
def get_sets(entry) -> List[dict]:
    green_pattern = re.compile(r'(\d+)\s+green')
    red_pattern = re.compile(r'(\d+)\s+red')
    blue_pattern = re.compile(r'(\d+)\s+blue')

    results = entry.split('; ')
    sets: List[dict] = []

    for r in results: 
        green_match = green_pattern.search(r)
        red_match = red_pattern.search(r)
        blue_match = blue_pattern.search(r)

        set_dict = {"red": 0, "green": 0, "blue": 0}

        if green_match:
            set_dict["green"] = int(green_match.group(1))
        if red_match:
            set_dict["red"] = int(red_match.group(1))
        if blue_match:
            set_dict["blue"] = int(blue_match.group(1))
        sets.append(set_dict)
    return sets


def read_file(file_name) -> GameProcess:
    game_sets: List[GameSet] = []
    with open(file_name, 'r') as file:
        for line in file:
            game_id: int = get_game_id(line)
            sets_colores: List[dict] = get_sets(line)
            
            records = []
            for set_color in sets_colores:
                red = set_color.get('red', 0)
                green = set_color.get('green', 0)
                blue = set_color.get('blue', 0)

                records.append(GameRecord(red=red, green=green, blue=blue))

            game_set: GameSet = GameSet(game_id, records)
            game_sets.append(game_set)

    return GameProcess(game_sets)

txt_file = 'data.txt'
game_process: GameProcess = read_file(txt_file)
result: int = game_process.process_valid_games()
total_power: int = game_process.get_sets_power_total()
print(f"The valid result is: {result}")
print(f"The total power is: {total_power}")

end_time = time.time()

execution_time = end_time - start_time

print(f"El programa tardó {execution_time} segundos en ejecutarse.")
