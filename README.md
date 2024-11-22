# Тренажер Печати

Тренажер Печати — это простое приложение для улучшения скорости и точности печати. Оно поддерживает несколько режимов и предоставляет обратную связь в реальном времени о вашей производительности.

## Функции

- Поддержка нескольких режимов печати: на скорость, ограниченное по времени и основанное на количестве слов.
- Обратная связь в реальном времени о скорости и точности печати.
- Визуальное выделение правильных и неправильных символов.
- Легкий переход между режимами с помощью клавиш.

## Установка

Этот проект использует только стандартные библиотеки Python, поэтому дополнительные установки не требуются.

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/usmon1/Usmon-PProject-2024.git
    cd Usmon-PProject-2024
    ```

2. Запустите приложение:

    ```sh
    python3 main.py
    ```

## Использование

1. **Запуск Приложения**: Запустите `main.py`, чтобы начать работу с приложением.
2. **Выбор Режима**: Используйте радиокнопки или клавиши стрелок влево и вправо для выбора режима печати.
3. **Начало Печати**: Нажмите кнопку "Start" или клавишу Enter, чтобы начать печатать.
4. **Обратная Связь в Реальном Времени**: По мере печати приложение будет отображать вашу скорость и точность в реальном времени. Правильные символы будут выделены синим цветом, а неправильные — красным.
5. **Завершение Сессии**: Нажмите кнопку "Stop" или клавишу Esc, чтобы завершить сессию и увидеть результаты.

## Запуск Тестов

Для запуска тестов используйте следующую команду:

```sh
python3 -m unittest discover -s tests
```
## Структура Директорий

```sh
~/Usmon-PProject-2024/
├── main.py                      # Главная точка входа для приложения
├── requirements.txt             # (Опционально) Список зависимостей, если есть
├── README.md                    # Документация
├── modes/                       # Директория с текстовыми файлами для различных режимов
│   ├── speed_mode.txt
│   ├── limit_time_mode.txt
│   ├── 10_word_mode.txt
│   ├── 15_word_mode.txt
│   ├── 20_word_mode.txt
│   └── 30_word_mode.txt
├── src/                         # Директория с исходным кодом
│   ├── __init__.py              # Отмечает директорию как пакет Python
│   ├── app.py                   # Главный класс приложения
│   ├── mode_manager.py          # Логика управления режимами
│   ├── typing_session.py        # Логика сессии печати
│   ├── result_manager.py         # Логика расчета результатов
│   └── ui_manager.py            # Управление пользовательским интерфейсом
└── tests/                       # Директория для тестов
    ├── __init__.py              # Отмечает директорию как пакет Python
    ├── test_mode_manager.py     # Тесты для mode_manager.py
    ├── test_typing_session.py   # Тесты для typing_session.py
    └── test_result_manager.py   # Тесты для result_manager.py
```

## Взаимодействие Классов

### Главная Точка Входа: `main.py`

- **Описание**: Точка входа для запуска приложения.
- **Импортирует и инициализирует**: `TypingTrainerApp` из `src/app.py`.

### Главный Контроллер: `TypingTrainerApp` (`src/app.py`)

- **Описание**: Управляет логикой всего приложения.
- **Инициализирует ключевые компоненты**:
  - `ModeManager` для управления режимами.
  - `UIManager` для интерфейса.
  - `TypingSession` для отслеживания текущей попытки.
  - `ResultManager` для обработки результатов.
- **Реагирует на события**:
  - Нажатие кнопок, переключение режимов.

### Управление Режимами: `ModeManager` (`src/mode_manager.py`)

- **Описание**: Хранит информацию о режимах и файлах.
- **Методы**:
  - `get_modes()`: Возвращает список доступных режимов.
  - `load_text(mode)`: Загружает строку из файла для текущего режима.

### Управление Сессией Печати: `TypingSession` (`src/typing_session.py`)

- **Описание**: Отслеживает прогресс текущей попытки.
- **Методы**:
  - `start(text)`: Начинает новую сессию с заданным текстом.
  - `update(input_text)`: Обновляет состояние сессии на основе введенного текста.
  - `end()`: Завершает сессию и возвращает результаты.
  - `get_speed()`: Возвращает текущую скорость печати.
  - `get_time()`: Возвращает текущее время сессии.
  - `is_complete()`: Проверяет, завершена ли сессия.

### Обработка Результатов: `ResultManager` (`src/result_manager.py`)

- **Описание**: Обрабатывает результаты сессии печати.
- **Методы**:
  - `calculate_results(data)`: Принимает данные о сессии и рассчитывает результаты.
  - `get_results()`: Возвращает результаты.

### Управление Пользовательским Интерфейсом: `UIManager` (`src/ui_manager.py`)

- **Описание**: Управляет интерфейсом пользователя.
- **Методы**:
  - `create_widgets()`: Создает виджеты интерфейса.
  - `bind_keys()`: Привязывает клавиши для управления интерфейсом.
  - `configure_styles()`: Настраивает стили виджетов.
  - `start_typing_session(typing_session)`: Начинает сессию печати.
  - `update_typing_session(event)`: Обновляет состояние сессии печати.
  - `highlight_text(current_text, input_text)`: Выделяет правильные и неправильные символы.
  - `update_timer()`: Обновляет таймер сессии.
  - `end_typing_session(event)`: Завершает сессию печати и отображает результаты.
  - `show_results(results)`: Отображает результаты сессии.

# Typing Trainer

Typing Trainer is a simple application to improve your typing speed and accuracy. It supports multiple modes and provides real-time feedback on your performance.

## Features

- Multiple typing modes: speed, time-limited, and word count-based.
- Real-time feedback on typing speed and accuracy.
- Visual highlighting of correct and incorrect characters.
- Easy mode switching using keyboard shortcuts.

## Installation

This project uses only standard Python libraries, so no additional installations are required.

1. Clone the repository:

    ```sh
    git clone https://github.com/usmon1/Usmon-PProject-2024.git
   cd Usmon-PProject-2024 
   ```

2. Run the application:

    ```sh
    python3 main.py
    ```

## Usage

1. **Start the Application**: Run `main.py` to start the application.
2. **Select a Mode**: Use the radio buttons or the left and right arrow keys to select a typing mode.
3. **Start Typing**: Click the "Start" button or press Enter to start typing.
4. **Real-time Feedback**: As you type, the application will display your speed and accuracy in real-time. Correct characters will be highlighted in blue, and incorrect characters will be highlighted in red.
5. **End Session**: Click the "Stop" button or press Esc to end the session and view your results.

## Running Tests

To run the tests, use the following command:

```sh
python3 -m unittest discover -s tests
```
## Directory Structure

```sh
~/Usmon-PProject-2024/
├── main.py                      # Main entry point for the application
├── requirements.txt             # (Optional) List of dependencies, if any
├── README.md                    # Documentation
├── modes/                       # Directory with text files for different modes
│   ├── speed_mode.txt
│   ├── limit_time_mode.txt
│   ├── 10_word_mode.txt
│   ├── 15_word_mode.txt
│   ├── 20_word_mode.txt
│   └── 30_word_mode.txt
├── src/                         # Source code directory
│   ├── __init__.py              # Marks the directory as a Python package
│   ├── app.py                   # Main application class
│   ├── mode_manager.py          # Mode management logic
│   ├── typing_session.py        # Typing session logic
│   ├── result_manager.py         # Result calculation logic
│   └── ui_manager.py            # User interface management
└── tests/                       # Directory for tests
    ├── __init__.py              # Marks the directory as a Python package
    ├── test_mode_manager.py     # Tests for mode_manager.py
    ├── test_typing_session.py   # Tests for typing_session.py
    └── test_result_manager.py   # Tests for result_manager.py
```

## Class Interactions

### Main Entry Point: `main.py`

- **Description**: The entry point to start the application.
- **Imports and Initializes**: `TypingTrainerApp` from `src/app.py`.

### Main Controller: `TypingTrainerApp` (`src/app.py`)

- **Description**: Manages the logic of the entire application.
- **Initializes Key Components**:
  - `ModeManager` for managing modes.
  - `UIManager` for the interface.
  - `TypingSession` for tracking the current attempt.
  - `ResultManager` for handling results.
- **Responds to Events**:
  - Button clicks, mode switching.

### Mode Management: `ModeManager` (`src/mode_manager.py`)

- **Description**: Stores information about modes and files.
- **Methods**:
  - `get_modes()`: Returns a list of available modes.
  - `load_text(mode)`: Loads a string from a file for the current mode.

### Typing Session Management: `TypingSession` (`src/typing_session.py`)

- **Description**: Tracks the progress of the current attempt.
- **Methods**:
  - `start(text)`: Starts a new session with the given text.
  - `update(input_text)`: Updates the session state based on the input text.
  - `end()`: Ends the session and returns the results.
  - `get_speed()`: Returns the current typing speed.
  - `get_time()`: Returns the current session time.
  - `is_complete()`: Checks if the session is complete.

### Result Handling: `ResultManager` (`src/result_manager.py`)

- **Description**: Handles the results of the typing session.
- **Methods**:
  - `calculate_results(data)`: Takes session data and calculates the results.
  - `get_results()`: Returns the results.

### User Interface Management: `UIManager` (`src/ui_manager.py`)

- **Description**: Manages the user interface.
- **Methods**:
  - `create_widgets()`: Creates the interface widgets.
  - `bind_keys()`: Binds keys for controlling the interface.
  - `configure_styles()`: Configures the styles of the widgets.
  - `start_typing_session(typing_session)`: Starts the typing session.
  - `update_typing_session(event)`: Updates the typing session state.
  - `highlight_text(current_text, input_text)`: Highlights correct and incorrect characters.
  - `update_timer()`: Updates the session timer.
  - `end_typing_session(event)`: Ends the typing session and displays the results.
  - `show_results(results)`: Displays the session results.


