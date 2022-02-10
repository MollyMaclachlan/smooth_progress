class ProgressBarClosedError(Exception):
    """This exception indicates that a call has been made which requires the ProgressBar
    to be open, however the ProgressBar was closed at the time.
    """
    def __init__(self: object, call: str):
        super().__init__(f"{call} was called, but ProgressBar is closed.")