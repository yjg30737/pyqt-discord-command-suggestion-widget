from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QTextEdit


class ChatBrowser(QScrollArea):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        lay = QVBoxLayout()
        lay.setAlignment(Qt.AlignTop)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(lay)
        self.setWidget(widget)
        self.setWidgetResizable(True)

    def showText(self, text):
        chatLbl = QLabel(text)
        chatLbl.setWordWrap(True)
        chatLbl.setTextInteractionFlags(Qt.TextSelectableByMouse)
        lay = self.widget().layout()
        if lay.count() % 2 == 0:
            chatLbl.setStyleSheet('QLabel { padding: 1em }')
            chatLbl.setAlignment(Qt.AlignLeft)
        else:
            chatLbl.setStyleSheet('QLabel { background-color: #DDD; padding: 1em }')
            chatLbl.setAlignment(Qt.AlignLeft)
        lay.addWidget(chatLbl)

    def event(self, e):
        if e.type() == 43:
            self.verticalScrollBar().setSliderPosition(self.verticalScrollBar().maximum())
        return super().event(e)