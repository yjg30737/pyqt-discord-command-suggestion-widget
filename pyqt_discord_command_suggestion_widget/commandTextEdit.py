from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal


class CommandTextEdit(QTextEdit):
    returnPressed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__initVal()

    def __initVal(self):
        self.setMaximumHeight(100)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            if e.modifiers() == Qt.ShiftModifier:
                return super().keyPressEvent(e)
            else:
                self.returnPressed.emit()
        else:
            return super().keyPressEvent(e)
