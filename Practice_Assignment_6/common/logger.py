import json


class Logger:
    """ Small class that manages logging """

    def __init__(self, filename: str):
        """ Initializer: clean logs if file exists or else create it """
        self._filename = filename
        with open(self._filename, "w"):
            pass

    def print_to_file(self, event, *args, **kwargs):
        """
        Printing log (with using json for convenience)
        :param event: event name
        :param args: unexpected positional arguments for event
        :param kwargs: keyword arguments, crucial for event
        """
        with open(self._filename, "at") as file:
            obj = dict({event: args}, **kwargs)
            json.dump(obj, file, indent=4, default=str)
            file.write("\n")
        return
