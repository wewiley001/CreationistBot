import sys
import os
import importlib.util
import ast
import time
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QComboBox,
    QPushButton, QListWidget, QLineEdit, QCheckBox, QMessageBox,
    QTextEdit, QScrollArea, QFrame
)
from PyQt5.QtGui import QTextCursor, QColor, QTextCharFormat
from PyQt5.QtCore import Qt

class MyForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stellaris - Game Testing Bot")
        self.setGeometry(100, 100, 1000, 600)

        # UI elements
        self.label = QLabel("Choose Game Script")
        self.dropdown_scripts = QComboBox()
        self.label_functions = QLabel("Select Function")
        self.dropdown_functions = QComboBox()
        self.confirm_button = QPushButton("Confirm Selection")
        self.run_button = QPushButton("Run Queue")
        self.clear_button = QPushButton("Clear Queue")
        self.label_wait = QLabel("Wait before execution (seconds):")
        self.input_wait = QLineEdit("0")
        self.loop_checkbox = QCheckBox("Loop queue continuously")
        self.queue_list = QListWidget()

        self.log_screen = QTextEdit()
        self.log_screen.setReadOnly(True)
        self.log_screen.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.log_screen.setMinimumHeight(150)
        self.log_screen.setStyleSheet("background-color: #111; color: #DDD;")

        self.label_functions.hide()
        self.dropdown_functions.hide()
        self.confirm_button.hide()
        self.run_button.hide()
        self.clear_button.hide()
        self.queue_list.hide()
        self.label_wait.hide()
        self.input_wait.hide()
        self.loop_checkbox.hide()
        self.log_screen.hide()

        # Queue list
        self.queued_functions = []

        # Populate dropdown with .py files from 'scripts' subfolder
        script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')
        self.script_dir = script_dir
        if os.path.exists(script_dir):
            scripts = [f for f in os.listdir(script_dir) if f.endswith(".py")]
            self.dropdown_scripts.addItem("")  # Default blank item
            self.dropdown_scripts.addItems(scripts)

        self.dropdown_scripts.currentIndexChanged.connect(self.on_script_select)
        self.confirm_button.clicked.connect(self.on_confirm)
        self.run_button.clicked.connect(self.run_queue)
        self.clear_button.clicked.connect(self.clear_queue)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.dropdown_scripts)
        layout.addWidget(self.label_functions)
        layout.addWidget(self.dropdown_functions)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.queue_list)
        layout.addWidget(self.label_wait)
        layout.addWidget(self.input_wait)
        layout.addWidget(self.loop_checkbox)
        layout.addWidget(self.run_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(QLabel("Execution Log:"))
        layout.addWidget(self.log_screen)

        self.setLayout(layout)

    def on_script_select(self):
        selected_script = self.dropdown_scripts.currentText()
        if not selected_script.strip():
            self.label_functions.hide()
            self.dropdown_functions.hide()
            self.confirm_button.hide()
            return

        script_path = os.path.join(self.script_dir, selected_script)
        functions = self.get_function_names(script_path)

        self.dropdown_functions.clear()
        if functions:
            self.dropdown_functions.addItems(functions)
            self.label_functions.show()
            self.dropdown_functions.show()
            self.confirm_button.show()
        else:
            self.label_functions.hide()
            self.dropdown_functions.hide()
            self.confirm_button.hide()

    def on_confirm(self):
        script = self.dropdown_scripts.currentText()
        func = self.dropdown_functions.currentText()
        if script and func:
            self.queued_functions.append((script, func))
            self.queue_list.addItem(f"{script}.{func}()")
            self.queue_list.show()
            self.label_wait.show()
            self.input_wait.show()
            self.loop_checkbox.show()
            self.run_button.show()
            self.clear_button.show()
            self.log_screen.show()

    def run_queue(self):
        try:
            wait_time = int(self.input_wait.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number of seconds to wait.")
            return

        if wait_time > 0:
            self.append_log(f"Waiting {wait_time} seconds before starting queue...", color='gray')
            time.sleep(wait_time)

        looping = self.loop_checkbox.isChecked()
        while True:
            for script, func_name in self.queued_functions:
                script_path = os.path.join(self.script_dir, script)
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                try:
                    spec = importlib.util.spec_from_file_location("module.name", script_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    func = getattr(module, func_name, None)
                    if callable(func):
                        self.append_log(f"[{timestamp}] Running: {script}.{func_name}()", color='cyan')
                        func()
                        self.append_log(f"[{timestamp}] Success: {script}.{func_name}() completed", color='green')
                    else:
                        self.append_log(f"[{timestamp}] Error: Function {func_name} not found in {script}.", color='red')
                except Exception as e:
                    self.append_log(f"[{timestamp}] Exception running {script}.{func_name}(): {e}", color='red')

            if not looping:
                break

    def clear_queue(self):
        self.queued_functions.clear()
        self.queue_list.clear()
        self.queue_list.hide()
        self.run_button.hide()
        self.clear_button.hide()
        self.label_wait.hide()
        self.input_wait.hide()
        self.loop_checkbox.hide()
        self.log_screen.clear()
        self.log_screen.hide()

    def append_log(self, message, color='white'):
        cursor = self.log_screen.textCursor()
        cursor.movePosition(QTextCursor.End)

        fmt = QTextCharFormat()
        color_map = {
            'red': QColor(Qt.red),
            'green': QColor(Qt.green),
            'cyan': QColor(Qt.cyan),
            'gray': QColor(Qt.lightGray),
            'white': QColor(Qt.white)
        }
        fmt.setForeground(color_map.get(color, QColor(Qt.white)))
        cursor.insertText(message + '\n', fmt)

        self.log_screen.setTextCursor(cursor)
        self.log_screen.ensureCursorVisible()
        print(message)

    def get_function_names(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                source = file.read()
                tree = ast.parse(source, filename=file_path)
                return [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return []

# Run the app
app = QApplication(sys.argv)
form = MyForm()
form.show()
sys.exit(app.exec_())
