import unittest
from src.typing_session import TypingSession

class TestTypingSession(unittest.TestCase):
    def setUp(self):
        self.session = TypingSession()
        self.text = "The quick brown fox jumps over the lazy dog."
        self.session.start(self.text)

    def test_start(self):
        self.assertEqual(self.session.get_text(), self.text)
        self.assertGreater(self.session.start_time, 0)

    def test_update(self):
        self.session.update("The quick brown")
        self.assertEqual(self.session.current_input, "The quick brown")
        self.assertEqual(self.session.correct_chars, 15)

    def test_end(self):
        self.session.update(self.text)
        results = self.session.end()
        self.assertGreater(results['speed'], 0)
        self.assertGreater(results['time'], 0)
        self.assertEqual(results['accuracy'], 100)

    def test_is_complete(self):
        self.session.update(self.text)
        self.assertTrue(self.session.is_complete())

if __name__ == '__main__':
    unittest.main()
