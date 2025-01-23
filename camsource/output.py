import threading
from picamera2.outputs import Output

class MTOutput(Output):
    def __init__(self, frameCallback):
        self.frameCallback = frameCallback
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

    def outputframe(self, frame, keyframe=True, timestamp=None, packet=None, audio=False):
        with self.lock:
            self.frame = frame
        with self.cond:
            self.cond.notify_all()

    def getFrame(self):
        with self.lock:
            return self.frame
