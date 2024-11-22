import tkinter as tk
from src.mode_manager import ModeManager
from src.ui_manager import UIManager
from src.typing_session import TypingSession
from src.result_manager import ResultManager

class TypingTrainerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Trainer")

        self.mode_manager = ModeManager()
        self.ui_manager = UIManager(self.root, self.start_session, self.mode_manager.get_modes())
        self.typing_session = TypingSession()
        self.result_manager = ResultManager()

        self.ui_manager.set_start_callback(self.start_session)

    def run(self):
        self.root.mainloop()

    def start_session(self):
        mode = self.ui_manager.get_selected_mode()
        text = self.mode_manager.load_text(mode)
        self.typing_session.start(text)
        self.ui_manager.start_typing_session(self.typing_session)

    def end_session(self):
        results = self.typing_session.end()
        self.result_manager.calculate_results(results)
        self.ui_manager.show_results(self.result_manager.get_results())
