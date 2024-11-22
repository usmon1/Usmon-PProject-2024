import unittest
from src.result_manager import ResultManager

class TestResultManager(unittest.TestCase):
    def setUp(self):
        self.result_manager = ResultManager()

    def test_calculate_results(self):
        data = {
            "speed": 50,
            "time": 60,
            "accuracy": 95
        }
        self.result_manager.calculate_results(data)
        results = self.result_manager.get_results()
        self.assertEqual(results['speed'], 50)
        self.assertEqual(results['time'], 60)
        self.assertEqual(results['accuracy'], 95)

if __name__ == '__main__':
    unittest.main()
