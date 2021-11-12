import json


class InterfaceMessages:
    """ Class for Interface Messages storing """

    def __init__(self, **kwargs):
        """
        Initializes InterfaceMessages object for convenience
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, item):
        return getattr(self, item, "lorem ipsum")


def prepare_messages(filename):
    """
    Prepare messages from file
    """
    with open(filename, "rt", encoding="UTF-8") as file:
        messages = json.load(file)

    return InterfaceMessages(**messages)
