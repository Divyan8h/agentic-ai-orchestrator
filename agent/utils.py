import signal
import time

class TimeoutException(Exception): 
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

def execute_with_timeout(func, seconds=5, *args, **kwargs):
    """
    Executes a function with a timeout.
    """
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)
    try:
        return func(*args, **kwargs)
    finally:
        signal.alarm(0)

def time_execution(func, *args, **kwargs):
    """
    Returns result + execution time
    """
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = round(time.time() - start, 3)
    return result, elapsed
