import cv2

class Camera:
    def __init__(self) -> None:
        self._webcam=cv2.VideoCapture(0)
    @property
    def frame(self):
        ret,rframe = self._webcam.read()
        return rframe