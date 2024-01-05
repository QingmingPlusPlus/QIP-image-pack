from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QSizePolicy, QLabel, QFileDialog
from src.signal.EventBus import EventBus


class HeaderSelector(QWidget):
    path_input = None
    browser_button = None
    confirm_button = None

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.state = HeaderSelectorState(self)
        self.init_action()

    def init_ui(self):
        self.setFixedHeight(50)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.path_input = QLineEdit()
        self.browser_button = QPushButton('浏览')
        self.confirm_button = QPushButton('确认')
        self.path_input.setFocusPolicy(Qt.ClickFocus)

        layout = QHBoxLayout(self)
        path_label = QLabel('路径：')
        layout.addWidget(path_label)
        layout.addWidget(self.path_input)
        layout.addWidget(self.browser_button)
        layout.addWidget(self.confirm_button)

    def init_action(self):
        self.browser_button.clicked.connect(self.state.on_browser_button_clicked)
        self.path_input.textChanged.connect(self.state.set_path_text)
        self.confirm_button.clicked.connect(self.state.on_search_button_clicked)


class HeaderSelectorState:
    __path_text = ''
    __widget = None

    def __init__(self, widget):
        self.__widget = widget

    def on_browser_button_clicked(self):
        folder_path = QFileDialog.getExistingDirectory(self.__widget, "选择文件夹")
        if folder_path:
            self._update_path_input_text(folder_path)

    def on_search_button_clicked(self):
        EventBus.path_selected.emit(self.__path_text)

    def set_path_text(self, path_text):
        self.__path_text = path_text
        EventBus.path_selected.emit(path_text)

    def _update_path_input_text(self, path_text: str):
        self.__widget.path_input.setText(path_text)
