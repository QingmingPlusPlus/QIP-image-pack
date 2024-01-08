from PySide6.QtWidgets import QWidget, QSizePolicy
from src.signal.EventBus import EventBus
from src.utils.path import is_folder_path, get_images_in_folder


class PreviewMonitor(QWidget):
    img_list: list[str] = []

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_action()

    def init_ui(self):
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def init_action(self):
        EventBus.path_selected.connect(self._on_path_selected)

    def _on_path_selected(self, path: str):
        if not is_folder_path(path):
            return
        self.img_list = get_images_in_folder(path)
