import threading
import time
from enum import Enum


class ConnectionStateChecker(object):
    def __init__(self, ping_function, keep_alive_interval, sleep=1):
        self.sleep = sleep
        self.keep_alive_interval = keep_alive_interval
        self.last_message = time.time()
        self.ping_function = ping_function
        self.running = False
        self._thread = None

    def start(self):
        self.running = True
        self._thread = threading.Thread(target=self.run)
        self._thread.daemon = True
        self._thread.start()

    def run(self):
        while self.running:
            time.sleep(self.sleep)
            time_without_messages = time.time() - self.last_message
            if self.keep_alive_interval < time_without_messages:
                self.ping_function()

    def stop(self):
        self.running = False


class ReconnectionType(Enum):
    raw = 0  # Reconnection with max reconnections and constant sleep time
    interval = 1  # variable sleep time
    exponential = 2  # exponential backoff


class ReconnectionHandler(object):
    def __init__(self):
        self.reconnecting = False
        self.attempt_number = 0
        self.last_attempt = time.time()

    def next(self):
        raise NotImplementedError()

    def reset(self):
        self.attempt_number = 0
        self.reconnecting = False


class RawReconnectionHandler(ReconnectionHandler):
    def __init__(self, sleep_time, max_attempts):
        super(RawReconnectionHandler, self).__init__()
        self.sleep_time = sleep_time
        self.max_reconnection_attempts = max_attempts

    def next(self):
        self.reconnecting = True
        if self.max_reconnection_attempts is not None:
            if self.attempt_number <= self.max_reconnection_attempts:
                self.attempt_number += 1
                return self.sleep_time
            else:
                raise ValueError(
                    "Max attempts reached {0}".format(self.max_reconnection_attempts)
                )
        else:  # Infinite reconnect
            return self.sleep_time


class ExponentialReconnectionHandler(ReconnectionHandler):
    def __init__(self, sleep_time, max_interval, max_attempts):
        super(ExponentialReconnectionHandler, self).__init__()
        self.sleep_time = sleep_time
        self.max_backoff = max_interval
        self.max_reconnection_attempts = max_attempts

    def next(self):
        self.reconnecting = True
        if (
            self.max_reconnection_attempts is not None
            and self.attempt_number >= self.max_reconnection_attempts
        ):
            raise ValueError(
                "Max attempts reached {0}".format(self.max_reconnection_attempts)
            )

        proposed_sleep = self.sleep_time ** (self.attempt_number + 1)
        self.attempt_number += 1
        if self.max_backoff is not None and proposed_sleep > self.max_backoff:
            proposed_sleep = self.max_backoff
            # Prevent unnecessary crazy exponentiation that could be really slow
            if self.max_reconnection_attempts is None:
                self.attempt_number -= 1
        return proposed_sleep


class IntervalReconnectionHandler(ReconnectionHandler):
    def __init__(self, intervals):
        super(IntervalReconnectionHandler, self).__init__()
        self._intervals = intervals

    def next(self):
        self.reconnecting = True
        index = self.attempt_number
        self.attempt_number += 1
        if index >= len(self._intervals):
            raise ValueError("Max intervals reached {0}".format(self._intervals))
        return self._intervals[index]
