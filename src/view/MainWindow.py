from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from src.view.HeaderSelector import HeaderSelector
from src.view.PreviewMonitor import PreviewMonitor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QIP')
        self.setGeometry(0, 0, 1920, 1080)

        central_widget = QWidget(self)
        header_selector = HeaderSelector()
        preview_monitor = PreviewMonitor()

        v_layout = QVBoxLayout(central_widget)
        v_layout.addWidget(header_selector)
        v_layout.addWidget(preview_monitor)

        self.setCentralWidget(central_widget)
        self.showMaximized()
