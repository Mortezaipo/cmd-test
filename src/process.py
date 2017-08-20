"""Process pooling management library."""

#import multiprocessing
#import threading


### Process which should run jobs in new thread
class Process:
    def __init__(self, name):
        self._name = name

    def add_new_child(self, job):
        pass

    def add_new_process_child(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


#class Thread(threading.Thread):
#    pass


#class Process(multiprocessing.Process):
#    pass


