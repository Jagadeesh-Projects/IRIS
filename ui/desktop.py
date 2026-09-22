from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit
)

from core.orchestrator import Orchestrator


class IrisWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.orchestrator = Orchestrator()

        self.setWindowTitle("IRIS - Personal AI Assistant")

        self.setMinimumSize(700, 500)

        layout = QVBoxLayout()

        title = QLabel("IRIS")
        title.setStyleSheet(
            "font-size: 32px; font-weight: bold;"
        )

        subtitle = QLabel(
            "Context-Aware Agentic Personal Intelligence System"
        )

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        self.input_box = QLineEdit()

        self.input_box.setPlaceholderText(
            "Ask IRIS something..."
        )

        send_button = QPushButton("Send")

        send_button.clicked.connect(
            self.send_message
        )

        self.input_box.returnPressed.connect(
            self.send_message
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.chat)
        layout.addWidget(self.input_box)
        layout.addWidget(send_button)

        self.setLayout(layout)

    def send_message(self):

        user_input = self.input_box.text().strip()

        if not user_input:
            return

        self.chat.append(
            f"You: {user_input}"
        )

        response = self.orchestrator.process(
            user_input
        )

        self.chat.append(
            f"IRIS: {response}"
        )

        self.input_box.clear()