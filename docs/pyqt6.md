# PyQt6 Documentation

PyQt6 is a set of Python bindings for the cross-platform Qt application framework. It allows Python developers to create desktop applications with rich graphical user interfaces and access various Qt functionalities.

## Installation

### Using pip (Recommended)

```bash
pip install PyQt6
```

### From Source

```bash
# Download and extract source
sip-install

# Or with manual make steps
sip-build --no-make
make
make install
```

### Installation Options

```bash
# Various configuration options
--confirm-license
--dbus
--license-dir
--no-dbus-python
--no-designer-plugin
--no-qml-plugin
--no-tools
--qt-shared
```

## Quick Start

### Basic Application

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Application")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        button = QPushButton("Click Me!")
        button.clicked.connect(self.on_button_click)
        layout.addWidget(button)

        self.setLayout(layout)

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

### Timer Example

```python
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Timer not started")
label.show()

def update_label():
    label.setText("Timer fired!")

timer = QTimer()
timer.timeout.connect(update_label)
timer.setInterval(1000)  # 1 second
timer.start()

app.exec()
```

## Core Modules

### QtCore - Core Non-GUI Classes

```python
from PyQt6.QtCore import QTimer, QThread, QObject, pyqtSignal

# Timer usage
timer = QTimer()
timer.setInterval(1000)  # milliseconds
timer.setSingleShot(True)  # Fire only once
timer.timeout.connect(callback_function)
timer.start()

# Signals and slots
class MyClass(QObject):
    my_signal = pyqtSignal(str)

    def emit_signal(self):
        self.my_signal.emit("Hello World")
```

### QtWidgets - GUI Components

```python
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout,
    QGridLayout, QMessageBox, QFileDialog
)

# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Widgets
        self.label = QLabel("Enter text:")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Submit")

        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        # Connect signals
        self.button.clicked.connect(self.on_submit)

    def on_submit(self):
        text = self.line_edit.text()
        QMessageBox.information(self, "Info", f"You entered: {text}")
```

### QtGui - GUI-Related Classes

```python
from PyQt6.QtGui import QPixmap, QIcon, QPainter, QFont, QColor

# Working with images
pixmap = QPixmap("image.png")
label = QLabel()
label.setPixmap(pixmap)

# Custom painting
class CustomWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(255, 0, 0))
        painter.drawLine(0, 0, 100, 100)
        painter.end()
```

## Layouts

### Layout Types

```python
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout

# Vertical layout
v_layout = QVBoxLayout()
v_layout.addWidget(widget1)
v_layout.addWidget(widget2)

# Horizontal layout
h_layout = QHBoxLayout()
h_layout.addWidget(widget1)
h_layout.addWidget(widget2)

# Grid layout
grid_layout = QGridLayout()
grid_layout.addWidget(widget1, 0, 0)  # row, column
grid_layout.addWidget(widget2, 0, 1)
grid_layout.addWidget(widget3, 1, 0, 1, 2)  # row, col, rowspan, colspan

# Form layout
form_layout = QFormLayout()
form_layout.addRow("Name:", QLineEdit())
form_layout.addRow("Email:", QLineEdit())
```

## Event Handling

### Signals and Slots

```python
from PyQt6.QtCore import pyqtSignal, QObject

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def do_work(self):
        for i in range(100):
            # Do some work
            self.progress.emit(i)
        self.finished.emit()

# Connect signals
worker = Worker()
worker.finished.connect(lambda: print("Work finished!"))
worker.progress.connect(lambda value: print(f"Progress: {value}%"))
```

### Event Filters

```python
from PyQt6.QtCore import QEvent

class EventFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress:
            print(f"Key pressed: {event.key()}")
            return True  # Event handled
        return False  # Event not handled

# Install event filter
filter_obj = EventFilter()
widget.installEventFilter(filter_obj)
```

## Dialogs and Message Boxes

### Message Boxes

```python
from PyQt6.QtWidgets import QMessageBox

# Information dialog
QMessageBox.information(parent, "Title", "Information message")

# Warning dialog
QMessageBox.warning(parent, "Title", "Warning message")

# Question dialog
reply = QMessageBox.question(parent, "Title", "Are you sure?",
                           QMessageBox.StandardButton.Yes |
                           QMessageBox.StandardButton.No)

if reply == QMessageBox.StandardButton.Yes:
    print("User clicked Yes")
```

### File Dialogs

```python
from PyQt6.QtWidgets import QFileDialog

# Open file dialog
file_path, _ = QFileDialog.getOpenFileName(
    parent, "Open File", "", "Text Files (*.txt);;All Files (*)"
)

# Save file dialog
file_path, _ = QFileDialog.getSaveFileName(
    parent, "Save File", "", "Text Files (*.txt);;All Files (*)"
)

# Directory dialog
directory = QFileDialog.getExistingDirectory(parent, "Select Directory")
```

## Threading

### QThread Usage

```python
from PyQt6.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)

    def run(self):
        for i in range(100):
            # Simulate work
            self.msleep(50)  # Sleep for 50ms
            self.progress.emit(i)

        self.finished.emit("Work completed!")

# Usage
thread = WorkerThread()
thread.progress.connect(lambda value: print(f"Progress: {value}%"))
thread.finished.connect(lambda msg: print(msg))
thread.start()
```

## Graphics and Painting

### Custom Painting

```python
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt

class CustomWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)

        # Set pen and brush
        pen = QPen(QColor(255, 0, 0), 2)
        brush = QBrush(QColor(0, 255, 0))
        painter.setPen(pen)
        painter.setBrush(brush)

        # Draw shapes
        painter.drawRect(10, 10, 100, 50)
        painter.drawEllipse(150, 10, 100, 50)
        painter.drawLine(10, 100, 250, 100)

        painter.end()
```

### Graphics View Framework

```python
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtCore import QRectF

# Create scene and view
scene = QGraphicsScene()
view = QGraphicsView(scene)

# Add items to scene
rect_item = QGraphicsRectItem(QRectF(0, 0, 100, 50))
scene.addItem(rect_item)

# Add text
text_item = scene.addText("Hello, Graphics!")

view.show()
```

## Multimedia

### Audio Playback

```python
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl

# Create media player
player = QMediaPlayer()
audio_output = QAudioOutput()
player.setAudioOutput(audio_output)

# Set source and play
player.setSource(QUrl.fromLocalFile("audio.mp3"))
player.play()
```

### Video Playback

```python
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

# Create video widget and player
video_widget = QVideoWidget()
player = QMediaPlayer()
player.setVideoOutput(video_widget)

# Set source and play
player.setSource(QUrl("http://example.com/video.mp4"))
video_widget.show()
player.play()
```

## Network Programming

### HTTP Requests

```python
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt6.QtCore import QUrl

class NetworkManager(QObject):
    def __init__(self):
        super().__init__()
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.handle_response)

    def make_request(self, url):
        request = QNetworkRequest(QUrl(url))
        self.manager.get(request)

    def handle_response(self, reply):
        data = reply.readAll()
        print(f"Response: {data.data().decode()}")
        reply.deleteLater()
```

## QML Integration

### Loading QML Files

```python
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtGui import QGuiApplication

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.load(QUrl.fromLocalFile("main.qml"))

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())
```

### Exposing Python Objects to QML

```python
from PyQt6.QtQml import qmlRegisterType
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot

class Backend(QObject):
    dataChanged = pyqtSignal(str)

    @pyqtSlot(str)
    def process_data(self, data):
        # Process data
        result = data.upper()
        self.dataChanged.emit(result)

# Register type with QML
qmlRegisterType(Backend, "Backend", 1, 0, "Backend")
```

## Styling and Themes

### Style Sheets

```python
# Apply stylesheet to widget
widget.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        font-size: 16px;
        border-radius: 4px;
    }

    QPushButton:hover {
        background-color: #45a049;
    }

    QPushButton:pressed {
        background-color: #3d8b40;
    }
""")
```

### Application-wide Styling

```python
app = QApplication(sys.argv)
app.setStyleSheet("""
    QMainWindow {
        background-color: #f0f0f0;
    }

    QLabel {
        color: #333333;
        font-family: Arial, sans-serif;
    }
""")
```

## Best Practices

### Memory Management

```python
# Proper parent-child relationships
parent_widget = QWidget()
child_widget = QWidget(parent_widget)  # Will be deleted with parent

# Explicit deletion when needed
widget.deleteLater()
```

### Error Handling

```python
try:
    # PyQt operations
    file_path, _ = QFileDialog.getOpenFileName(self, "Open File")
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
except Exception as e:
    QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
```

### Performance Tips

1. Use `QTimer.singleShot()` for delayed operations
2. Implement lazy loading for large datasets
3. Use `QThread` for CPU-intensive tasks
4. Cache expensive operations
5. Use appropriate layout managers

## Common Patterns

### Model-View Architecture

```python
from PyQt6.QtCore import QAbstractListModel, Qt
from PyQt6.QtWidgets import QListView

class StringListModel(QAbstractListModel):
    def __init__(self, strings=None):
        super().__init__()
        self.strings = strings or []

    def rowCount(self, parent=None):
        return len(self.strings)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.strings[index.row()]
        return None

# Usage
model = StringListModel(["Item 1", "Item 2", "Item 3"])
view = QListView()
view.setModel(model)
```

### Settings Management

```python
from PyQt6.QtCore import QSettings

# Save settings
settings = QSettings("MyCompany", "MyApp")
settings.setValue("window/size", self.size())
settings.setValue("window/position", self.pos())

# Load settings
settings = QSettings("MyCompany", "MyApp")
size = settings.value("window/size", self.size())
position = settings.value("window/position", self.pos())
self.resize(size)
self.move(position)
```

This documentation covers the essential aspects of PyQt6 for creating desktop applications with rich graphical user interfaces.
