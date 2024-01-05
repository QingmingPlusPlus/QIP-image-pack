from PySide6.QtWidgets import QWidget, QSizePolicy
from src.signal.EventBus import EventBus


class PreviewMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_action()

    def init_ui(self):
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def init_action(self):
        EventBus.path_selected.connect(self._on_path_selected)

    def _on_path_selected(self, path: str):
        print("From event bus", path)
