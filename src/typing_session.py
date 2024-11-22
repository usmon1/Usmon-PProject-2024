import time

class TypingSession:
    def __init__(self):
        self.text = ""
        self.start_time = 0
        self.end_time = 0
        self.current_input = ""
        self.correct_chars = 0
        self.total_chars = 0
        self.is_active = False

    def start(self, text):
        self.text = text
        self.start_time = time.time()
        self.current_input = ""
        self.correct_chars = 0
        self.total_chars = len(text)
        self.is_active = True

    def update(self, input_text):
        if self.is_active:
            self.current_input = input_text
            correct_chars = sum(1 for a, b in zip(self.text, input_text) if a == b)
            self.correct_chars = correct_chars

    def end(self):
        if self.is_active:
            self.end_time = time.time()
            self.is_active = False
            return {
                "speed": self.calculate_speed(),
                "time": self.end_time - self.start_time,
                "accuracy": self.calculate_accuracy()
            }
        return {
            "speed": 0,
            "time": 0,
            "accuracy": 0
        }

    def calculate_speed(self):
        elapsed_time = self.end_time - self.start_time
        words_per_minute = (len(self.current_input.split()) / elapsed_time) * 60
        return words_per_minute

    def calculate_accuracy(self):
        if self.total_chars == 0:
            return 0
        return (self.correct_chars / self.total_chars) * 100

    def get_text(self):
        return self.text

    def get_speed(self):
        if self.is_active:
            elapsed_time = time.time() - self.start_time
            words_per_minute = (len(self.current_input.split()) / elapsed_time) * 60
            return words_per_minute
        return 0

    def get_time(self):
        if self.is_active:
            return int(time.time() - self.start_time)
        return 0

    def get_cursor(self):
        return self.current_input

    def get_results(self):
        return {
            "speed": self.calculate_speed(),
            "time": self.end_time - self.start_time,
            "accuracy": self.calculate_accuracy()
        }

    def is_complete(self):
        return len(self.current_input) >= len(self.text)
