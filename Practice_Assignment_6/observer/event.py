class Event(object):
    """
    Class for registering any kind event with preset observers
    Invokes observers (static field) when creating an instance
    """

    _observers = []

    def __init__(self, name, *args, **kwargs):
        """ Initializer: invoke a call after creating an instance """
        self.name = name
        self.args = args
        self.kwargs = kwargs

        self.callback()

    def callback(self):
        """ Invoke callbacks in observers """
        for observer in Event._observers:
            observer.callback(self)

    @staticmethod
    def add_observer(observer):
        """ Add observer to Event observers list """
        Event._observers.append(observer)
        return

    @staticmethod
    def remove_observer(observer):
        """ Remove observer from Event observer list """
        for i in range(len(Event._observers)):
            if observer is Event._observers[i] or observer == Event._observers[i]:
                Event._observers.pop(i)
                return
