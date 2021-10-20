from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    def __init__(self, e):
        super().__init__("Timeout Eorro ...")

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL,seconds) #used timer instead of alarm
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator


@timeout(3)
def testing():
    import time
    count = 0
    while count < 7:
        print('helloworld', count)
        count += 1
        time.sleep(1)
    return count

if __name__ == '__main__':
    count = 0

    while count < 5:
        try:
            testing()
            break
        except Exception as e:
            print('timeout occur', str(e))
            count += 1
