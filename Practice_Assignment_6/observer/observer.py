from observer.event import Event


class Observer:
    """
    Multi-task singleton-behavior event observer
    Class name is used as an object
    """

    _callbacks = dict()

    def __init__(self, event: str, callback):
        """ Initializer: link type of event and reactions to them """
        if event not in Observer._callbacks.keys():
            Observer._callbacks[event] = [callback]
        else:
            Observer._callbacks[event].append(callback)

    @staticmethod
    def callback(event: Event):
        """
        Invoke callback (used from Publisher, Event etc. class)
        :param event: type of event happened
        """
        curr_callbacks = Observer._callbacks[event.name]
        for callback in curr_callbacks:
            callback(event.name, *event.args, **event.kwargs)
        return
