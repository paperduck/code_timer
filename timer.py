import datetime
import timeit

class Timer():

    @classmethod
    def start(cls):
        """ Returns the wall clock time, in seconds """
        return timeit.default_timer()


    @classmethod
    def stop(cls, start):
        """ Returns the duration of time passed, in seconds.
        
        Parameters:
            start: float - return value of start()
        """
        return timeit.default_timer() - start
