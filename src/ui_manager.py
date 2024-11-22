import tkinter as tk
from tkinter import ttk

class UIManager:
    def __init__(self, root, start_callback, modes):
        self.root = root
        self.start_callback = start_callback
        self.modes = modes
        self.selected_mode = tk.StringVar(value=modes[0])
        self.typing_session = None
        self.timer_running = False
        self.limit_time_mode = False

        self.create_widgets()
        self.bind_keys()
        self.configure_styles()

    def create_widgets(self):
        self.mode_frame = ttk.Frame(self.root)
        self.mode_frame.pack(pady=10)

        for mode in self.modes:
            ttk.Radiobutton(self.mode_frame, text=mode, variable=self.selected_mode, value=mode, command=self.mode_changed).pack(side=tk.LEFT, padx=5)

        self.start_button = ttk.Button(self.root, text="Start->Enter", command=self.start_callback)
        self.start_button.pack(pady=10)
        self.root.bind("<Return>", lambda event: self.start_callback())

        self.stop_button = ttk.Button(self.root, text="Stop->Esc", command=self.end_typing_session)
        self.stop_button.pack(pady=10)
        self.root.bind("<Escape>", lambda event: self.end_typing_session())

        self.text_label = tk.Text(self.root, wrap='word', height=5, width=40, font=('Helvetica', 30))
        self.text_label.pack(pady=10)
        self.text_label.tag_configure("correct", foreground="blue")
        self.text_label.tag_configure("incorrect", foreground="red")

        self.input_entry = ttk.Entry(self.root)
        self.input_entry.pack(pady=10)

        self.speed_label = ttk.Label(self.root, text="Speed: 0 WPM")
        self.speed_label.pack(pady=10)

        self.timer_label = ttk.Label(self.root, text="Time: 0s")
        self.timer_label.pack(pady=10)

    def bind_keys(self):
        self.root.bind("<Right>", self.next_mode)
        self.root.bind("<Left>", self.prev_mode)

    def configure_styles(self):
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=('Helvetica', 12))
        style.configure("TRadiobutton", padding=6, relief="flat", background="#f0f0f0", foreground="black", font=('Helvetica', 12))
        style.configure("TLabel", padding=6, background="#f0f0f0", foreground="black", font=('Helvetica', 12))
        style.configure("TEntry", padding=6, relief="flat", background="white", foreground="black", font=('Helvetica', 12))

    def set_start_callback(self, callback):
        self.start_callback = callback

    def get_selected_mode(self):
        return self.selected_mode.get()

    def mode_changed(self):
        if self.typing_session:
            self.end_typing_session()

    def next_mode(self, event=None):
        current_index = self.modes.index(self.selected_mode.get())
        next_index = (current_index + 1) % len(self.modes)
        self.selected_mode.set(self.modes[next_index])
        self.mode_changed()

    def prev_mode(self, event=None):
        current_index = self.modes.index(self.selected_mode.get())
        prev_index = (current_index - 1) % len(self.modes)
        self.selected_mode.set(self.modes[prev_index])
        self.mode_changed()

    def start_typing_session(self, typing_session):
        self.typing_session = typing_session
        self.text_label.delete(1.0, tk.END)
        self.text_label.insert(tk.END, typing_session.get_text())
        self.input_entry.delete(0, tk.END)  # Очистка поля ввода
        self.input_entry.bind("<KeyRelease>", self.update_typing_session)
        self.input_entry.bind("<Return>", self.end_typing_session)
        self.timer_running = True
        self.limit_time_mode = (self.selected_mode.get() == "limit_time_mode")
        self.update_timer()

    def update_typing_session(self, event):
        self.typing_session.update(self.input_entry.get())
        self.speed_label.config(text=f"Speed: {self.typing_session.get_speed():.2f} WPM")

        # Выделение текста
        current_text = self.typing_session.get_text()
        input_text = self.input_entry.get()
        self.highlight_text(current_text, input_text)

        if self.typing_session.is_complete():
            self.end_typing_session(None)

    def highlight_text(self, current_text, input_text):
        self.text_label.delete(1.0, tk.END)
        self.text_label.insert(tk.END, current_text)
        input_len = len(input_text)
        for i in range(input_len):
            if current_text[i] == input_text[i]:
                self.text_label.tag_add("correct", f"1.{i}")
            else:
                self.text_label.tag_add("incorrect", f"1.{i}")

    def update_timer(self):
        if self.timer_running:
            if self.limit_time_mode:
                remaining_time = 60 - self.typing_session.get_time()
                if remaining_time <= 0:
                    self.end_typing_session()
                else:
                    self.timer_label.config(text=f"Time: {remaining_time}s")
                    self.root.after(1000, self.update_timer)
            else:
                self.timer_label.config(text=f"Time: {self.typing_session.get_time()}s")
                self.root.after(1000, self.update_timer)

    def end_typing_session(self, event=None):
        if self.typing_session:
            results = self.typing_session.end()
            self.show_results(results)
            self.timer_running = False
            self.input_entry.unbind("<KeyRelease>")
            self.input_entry.unbind("<Return>")
            self.input_entry.delete(0, tk.END)  # Очистка поля ввода

    def show_results(self, results):
        result_text = f"Speed: {results['speed']:.2f} WPM\nTime: {results['time']:.2f}s\nAccuracy: {results['accuracy']:.2f}%"
        self.text_label.delete(1.0, tk.END)
        self.text_label.insert(tk.END, result_text)
