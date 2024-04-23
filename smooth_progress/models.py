from math import floor
from .exceptions import ProgressBarClosedError

class ProgressBar:
    """
    The primary class for the ProgressBar. All control operations exist as methods of this class.
    Once the project is more completed, attributes will be hidden and available through getter and
    setter method pairs.
    """
    def __enter__(self):
        return self

    def __exit__(self, t, val, tb) -> None:
        del self

    def __init__(self, limit: int = 100, show_percent: bool = True) -> None:
        """
        :param limit: optional; default 100
        :param show_percent: optional; default True
        """
        self.count = None
        self.GRANULARITY = 50
        self.limit = limit
        self.opened = False
        self.show_percent = show_percent
        self.state = None

    def __update(self, completion: int, percentage: int) -> None:
        """
        Hidden method to update the state of the bar with new values. Should only be called from
        within the class itself.

        :param completion: the number of characters in the bar that are completed
        :param percentage: the percentage of characters in the bar that are completed
        """
        self.state = (
            f"[{'#' * completion}{'-' * (self.GRANULARITY - completion)}]"
            + f"  {str(self.count)}/{str(self.limit)}"
            + (f" [{percentage}%]" if self.show_percent else "")
        )

    def close(self) -> bool:
        """
        Closes the ProgressBar from mutability, displaying its final state before interruption.

        Note that a carriage return is executed BEFORE the final display; this ensures console
        outputs such as ^C from a Control+C SIGKILL will be overwritten.
        """
        if self.opened:
            self.show(display = "\r" + self.state, end = "\n", flush = False)
            self.opened = False
            return True
        else:
            return False

    def increment(self) -> None:
        """
        Increments the progress and updates the display to reflect the new value. If this
        incrementation takes the progress to the pre-defined limit, closes the ProgressBar from
        mutability.
        """
        if self.opened:
            self.count += 1
            fraction = self.count/self.limit
            self.__update(floor(fraction*self.GRANULARITY), floor(fraction*100))
            self.show()
            if self.count == self.limit:
                self.close()
        else:
            raise ProgressBarClosedError(".increment()")

    def interrupt(self) -> bool:
        """
        A more forceful version of close(); interrupts the ProgressBar by closing it from
        mutability, without displaying its final state.
        """
        if self.opened:
            self.opened = False
            self.show(display="")
            return True
        else:
            return False

    def open(self) -> bool:
        """
        Resets all progress and opens the ProgressBar to mutability, displaying its initial, empty
        state.
        """
        if self.opened:
            return False
        else:
            self.count = 0
            self.__update(0, 0)
            self.show()
            self.opened = True
            return True

    def show(self, display: str = None, end: str = "\r", flush: bool = True) -> None:
        """
        Display the current state of the bar, or some other defined content, with the end character
        determined by the call.

        :param display: the content to display, by default None, indicating that the current state
                        of the bar should be displayed
        :param end: the end character, by default a new line; only control characters are
                    recommended, but any string can be passed
        :param flush: whether to forcibly flush the stdout stream
        """
        print(self.state if display is None else display, end=end, flush=flush)
