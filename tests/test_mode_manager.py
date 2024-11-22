import unittest
from src.mode_manager import ModeManager

class TestModeManager(unittest.TestCase):
    def setUp(self):
        self.mode_manager = ModeManager()

    def test_get_modes(self):
        modes = self.mode_manager.get_modes()
        self.assertIn("speed_mode", modes)
        self.assertIn("limit_time_mode", modes)
        self.assertIn("10_word_mode", modes)
        self.assertIn("15_word_mode", modes)
        self.assertIn("20_word_mode", modes)
        self.assertIn("30_word_mode", modes)

    def test_load_text(self):
        text = self.mode_manager.load_text("speed_mode")
        self.assertIsNotNone(text)
        self.assertIsInstance(text, str)

if __name__ == '__main__':
    unittest.main()
