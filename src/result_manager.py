class ResultManager:
    def __init__(self):
        self.results = {}

    def calculate_results(self, data):
        self.results = data

    def get_results(self):
        return self.results
