from threading import Event


def init():
    global launchevent
    launchevent = Event()
    global timerevent
    timerevent = Event()
