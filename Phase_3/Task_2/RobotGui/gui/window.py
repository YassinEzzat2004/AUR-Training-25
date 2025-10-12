from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout,QSizePolicy
from RobotGui.gui.camera_display import CameraDisplay
from RobotGui.gui.coordinates_display import CoordinatesDisplay
from PySide6.QtCore import Qt
from RobotGui.core.comm.client import setup,move_command


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(640, 480)

        self.setCentralWidget(CentralWidget())

        self.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key=event.key()
        if key==Qt.Key.Key_Up:
            move_command('forward')
        elif key==Qt.Key.Key_Down:
            move_command('backward')
        elif key==Qt.Key.Key_Right:
            move_command('right')
        elif key==Qt.Key.Key_Left:
            move_command('left')
        else:
            pass
    
    

class CentralWidget(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self._layout = QVBoxLayout(self)
        self._camera_widget = CameraDisplay()
        self._layout.addWidget(self._camera_widget,2)

        self._coordinates_widget = CoordinatesDisplay()
        self._coordinates_widget.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        setup(self._coordinates_widget.update_coordinates)
        self._layout.addWidget(self._coordinates_widget,1)