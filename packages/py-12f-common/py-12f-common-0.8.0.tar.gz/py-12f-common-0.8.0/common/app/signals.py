"""
DelayedKeyboardInterrupt implementation.

This module is only internally used by the :class:`~common.app.app_base.ApplicationBase` class.
"""
import os
import signal


__all__ = [
    "SIGNAL_TRANSLATION_MAP",
]

SIGNAL_TRANSLATION_MAP = {
    signal.SIGINT: "SIGINT",
    signal.SIGTERM: "SIGTERM",
}


def add_term_signal_handler(logger, callback):
    """
    Register a callback function to catch the SIGINT and SIGTERM signals
    """

    def signal_cb_wrapper(callback):
        def fun(sig, frame):
            logger.info(f"signal: {sig}, frame: {frame}")
            callback()

        return fun

    signal.signal(signal.SIGINT, signal_cb_wrapper(callback))
    signal.signal(signal.SIGTERM, signal_cb_wrapper(callback))


class DelayedKeyboardInterrupt:
    """
    A context provider class, that makes possible to postpone the handling of exceptions
    that may occur inside the context.
    """

    def __init__(self, logger, propagate_to_forked_processes=None):
        """
        Constructs a context manager that suppresses SIGINT & SIGTERM signal handlers
        for a block of code.
        The signal handlers are called on exit from the block.
        Inspired by: https://stackoverflow.com/a/21919644
        :param propagate_to_forked_processes: This parameter controls behavior of this context manager
        in forked processes.
        If True, this context manager behaves the same way in forked processes as in parent process.
        If False, signals received in forked processes are handled by the original signal handler.
        If None, signals received in forked processes are ignored (default).
        """
        self.logger = logger
        self._pid = os.getpid()
        self._propagate_to_forked_processes = propagate_to_forked_processes
        self._sig = None
        self._frame = None
        self._old_signal_handler_map = None

    def __enter__(self):
        self._old_signal_handler_map = {
            sig: signal.signal(sig, self._handler)
            for sig, _ in SIGNAL_TRANSLATION_MAP.items()
        }

    def __exit__(self, exc_type, exc_val, exc_tb):
        for sig, handler in self._old_signal_handler_map.items():
            signal.signal(sig, handler)

        if self._sig is None:
            return

        self._old_signal_handler_map[self._sig](self._sig, self._frame)

    def _handler(self, sig, frame):
        self._sig = sig
        self._frame = frame

        #
        # Protection against fork.
        #
        if os.getpid() != self._pid:
            if self._propagate_to_forked_processes is False:
                self.logger.error(
                    f"!!! DelayedKeyboardInterrupt._handler: {SIGNAL_TRANSLATION_MAP[sig]} received; "
                    f"PID mismatch: {os.getpid()=}, {self._pid=}, calling original handler"
                )
                self._old_signal_handler_map[self._sig](self._sig, self._frame)
            elif self._propagate_to_forked_processes is None:
                self.logger.error(
                    f"!!! DelayedKeyboardInterrupt._handler: {SIGNAL_TRANSLATION_MAP[sig]} received; "
                    f"PID mismatch: {os.getpid()=}, ignoring the signal"
                )
                return
            # elif self._propagate_to_forked_processes is True:
            #   ... passthrough

        self.logger.error(
            f"!!! DelayedKeyboardInterrupt._handler: {SIGNAL_TRANSLATION_MAP[sig]} received; delaying KeyboardInterrupt"
        )
