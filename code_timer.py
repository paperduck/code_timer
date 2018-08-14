import datetime
import timeit

class CodeTimer():

    start = None

    @classmethod
    def start(cls):
        """ Record the wall clock time, in seconds """
        cls.start = timeit.default_timer()


    @classmethod
    def stop(cls):
        """ Returns the duration of time passed, in seconds."""
        if not cls.start:
            raise Exception
        duration = timeit.default_timer() - cls.start
        if duration < 0:
            duration += 60*60*24
        return duration
