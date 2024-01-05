from PySide6.QtCore import Signal, QObject


class __EventBus(QObject):
    path_selected = Signal(str)


EventBus = __EventBus()
