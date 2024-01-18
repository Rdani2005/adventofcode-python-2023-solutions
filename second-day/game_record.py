class GameRecord:
    def __init__(self, red = 0, blue = 0, green = 0):
        self.red = red
        self.blue = blue
        self.green = green
    
    def __str__(self):
        return f"({self.red}, {self.blue}, {self.green})"
    
    def validate_part_one(self):
        return self.red <= 12 and self.blue <= 14 and self.green <= 13