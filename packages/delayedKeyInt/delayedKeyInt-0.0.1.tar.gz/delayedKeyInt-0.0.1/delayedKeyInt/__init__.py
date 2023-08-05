import signal


# noinspection PyAttributeOutsideInit
class DelayedKeyboardInterrupt:
    """
DelayedKeyboardInterrupt:
    Use with a context manager to delay or suspend keyboard interrupts
    USAGE:
        with DelayedKeyboardInterrupt():
            #code will run then, if a keyboard interrupt is recieved, will raise KeyboardInterrupt
            code()
    """

    def __enter__(self):
        self.signal_received = False
        self.old_handler = signal.signal(signal.SIGINT, self.handler)

    def handler(self, sig, frame):
        self.signal_received = (sig, frame)

    def __exit__(self, type, value, traceback):
        signal.signal(signal.SIGINT, self.old_handler)
        if self.signal_received:
            self.old_handler(*self.signal_received)
