import random

class ModeManager:
    def __init__(self):
        self.modes = {
            "speed_mode": "modes/speed_mode.txt",
            "limit_time_mode": "modes/limit_time_mode.txt",
            "10_word_mode": "modes/10_word_mode.txt",
            "15_word_mode": "modes/15_word_mode.txt",
            "20_word_mode": "modes/20_word_mode.txt",
            "30_word_mode": "modes/30_word_mode.txt"
        }

    def get_modes(self):
        return list(self.modes.keys())

    def load_text(self, mode):
        with open(self.modes[mode], 'r') as file:
            lines = file.readlines()
            return random.choice(lines).strip()
