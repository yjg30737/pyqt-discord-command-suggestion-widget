import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSizePolicy

from pyqt_discord_command_suggestion_widget.chatWidget import ChatBrowser
from pyqt_discord_command_suggestion_widget.commandSuggestionWidget import CommandSuggestionWidget
from pyqt_discord_command_suggestion_widget.commandTextEdit import CommandTextEdit


class CommandSuggestionGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Command Suggestion GUI")

        # Create the main layout
        layout = QVBoxLayout()

        self.__chatWidget = ChatBrowser()

        # Create the command suggestion list
        self.suggestionWidget = CommandSuggestionWidget()
        self.suggestion_list = self.suggestionWidget.getCommandList()
        self.suggestion_list.itemClicked.connect(self.execute_command)
        self.suggestionWidget.setVisible(False)

        # Create the input field
        self.input_field = CommandTextEdit()
        self.input_field.returnPressed.connect(self.showText)
        self.input_field.textChanged.connect(self.update_suggestions)

        layout.addWidget(self.__chatWidget)
        layout.addWidget(self.suggestionWidget)
        layout.addWidget(self.input_field)

        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignBottom)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_suggestions(self):
        input_text_chunk = self.input_field.toPlainText().split()
        input_text_chunk_exists = len(input_text_chunk) > 0
        self.suggestionWidget.setVisible(input_text_chunk_exists)
        if input_text_chunk_exists:
            input_text_chunk = input_text_chunk[-1]
            starts_with_f = input_text_chunk.startswith('/')
            self.suggestionWidget.setVisible(starts_with_f)
            if starts_with_f:
                command_word = input_text_chunk[1:]

                # Example: Add some dummy command suggestions
                commands = 'Alberic Litte,Angalmo,Antus Odiil,Ariela Doran,Arriana Valga,Athragar,Bittneld the Curse-Bringer,Carmen Litte,Casta Scribonia,Chanel,Chorrol Jailor,Chorrol Soldier,City Watch,Dar-Ma,Earana,Emfrid,Estelle Renoit,Eugal Belette,Fighters Guild Porter,Francois Motierre,Gaturn gro-Gonk,Glistel,Gureryne Selvilo,Honditar,Jirolin Doran,Kurz gro-Baroth,Laythe Wavrick,Lazy Kaslowyn,Lum gro-Baroth,Malintus Ancrus,Modryn Oreyn,Nardhil,Nermus the Mooch,Orag gra-Bargol,Orgnolf Hairy-Legs,Orok gro-Ghoth,Otius Loran,Rallus Odiil,Rasheda,Rena Bruiant,Reynald Jemane,Rimalus Bruiant,Seed-Neeus,Talasma,Teekeeus,Valus Odiil,Vilena Donton,Wallace'.split()
                filtered_commands = commands
                if command_word:
                    filtered_commands = [command for command in commands if command_word.lower() in command.lower()]
                filtered_commands_exists_f = len(filtered_commands) > 0
                self.suggestionWidget.setVisible(filtered_commands_exists_f)
                if filtered_commands_exists_f:
                    # Clear previous suggestions
                    self.suggestion_list.clear()

                    # Add the filtered suggestions to the list
                    self.suggestion_list.addItems(filtered_commands)
                    self.suggestion_list.setCurrentRow(0)

    def showText(self):
        t = self.input_field.toPlainText()
        self.__chatWidget.showText(t)

    def execute_command(self, item):
        command = item.text()
        self.input_field.textCursor().deletePreviousChar()
        self.input_field.insertPlainText(command)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CommandSuggestionGUI()
    window.show()
    sys.exit(app.exec_())
