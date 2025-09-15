from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QApplication
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from ..core import Orchestrator

class CrewWorker(QThread):
    """
    A worker thread for running the CrewAI crew without blocking the GUI.
    """
    # Signal to emit the final result of the crew's work
    finished = pyqtSignal(str)
    # Signal to emit any errors that occur
    error = pyqtSignal(str)
    # Signal to emit real-time logs and progress updates
    log = pyqtSignal(str)

    def __init__(self, orchestrator: Orchestrator, user_request: str):
        super().__init__()
        self.orchestrator = orchestrator
        self.user_request = user_request

    def run(self):
        """
        The main entry point for the thread. This method will execute the
        long-running crew process.
        """
        try:
            # In a real application, the orchestrator would be designed to
            # stream logs back. For now, we'll just emit a start message.
            self.log.emit("Crew execution started...")

            # This is a blocking call, which is why it's in a thread.
            result = self.orchestrator.run_crew(self.user_request)

            self.log.emit("Crew execution finished.")
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(f"An error occurred in the crew: {e}")

class ChatWidget(QWidget):
    """
    The main chat interface widget for AURA. It includes a display area
    for the conversation and an input box for the user.
    """
    def __init__(self, orchestrator: Orchestrator):
        super().__init__()
        self.orchestrator = orchestrator
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type your message to AURA here...")
        self.input_box.returnPressed.connect(self.on_send_message)
        self.layout.addWidget(self.input_box)

    def on_send_message(self):
        """
        Handles the event when the user sends a message.
        """
        user_message = self.input_box.text().strip()
        if not user_message:
            return

        self.add_message("<b>You</b>", user_message)
        self.input_box.clear()

        # Disable input while the crew is working
        self.input_box.setEnabled(False)

        # Create and start the worker thread
        self.worker = CrewWorker(self.orchestrator, user_message)
        self.worker.finished.connect(self.on_crew_finished)
        self.worker.error.connect(self.on_crew_error)
        self.worker.log.connect(self.on_crew_log)
        self.worker.start()

    def add_message(self, sender: str, message: str):
        """
        Adds a message to the chat display with simple HTML formatting.
        """
        # Basic formatting for messages.
        formatted_message = f'<p><b>{sender}:</b> {message.replace(chr(10), "<br>")}</p>'
        self.chat_display.append(formatted_message)

        # Auto-scroll to the bottom
        self.chat_display.verticalScrollBar().setValue(self.chat_display.verticalScrollBar().maximum())

    def on_crew_finished(self, result: str):
        """
        Handles the successful completion of the crew's work.
        """
        self.add_message("<b>AURA</b>", result)
        self.input_box.setEnabled(True)
        self.input_box.setFocus()

    def on_crew_error(self, error_message: str):
        """
        Handles any errors that occur during the crew's execution.
        """
        detailed_error = (
            "An error occurred while processing your request. "
            "Please check the logs for more details.\n"
            f"Error: {error_message}"
        )
        self.add_message("<b>AURA (Error)</b>", detailed_error)
        self.input_box.setEnabled(True)
        self.input_box.setFocus()

    def on_crew_log(self, log_message: str):
        """
        Displays log messages from the crew's execution.
        """
        self.add_message("<i>Log</i>", log_message)
