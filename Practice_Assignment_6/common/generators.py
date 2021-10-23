import random


class GeneratingIterator:

    def __init__(self, count, *args, default_source=random.uniform, **kwargs):
        """
        Initializing generator via Python class
        :param count: how many elements to generate
        :param args: arguments to source function
        :param default_source: source function
        :param kwargs: keyword arguments to source function
        """
        self.count = count

        self.source = default_source
        self.source_args = args
        self.source_kwargs = kwargs

    def __iter__(self):
        """
        Dunder method of creating iterator via iter()
        :return:
        """
        # next is also called on first iteration, predict it
        self.index = -1
        return self

    def __next__(self):
        """
        Dunder method of iterating
        :return:
        """
        # coming to next "position"
        self.index += 1

        # stop when reached end
        if self.index == self.count:
            raise StopIteration

        else:
            # return a new generated value
            return self.source(*self.source_args, **self.source_kwargs)


def scan_from_file(filename, type_cast=str, encoding=None):
    """
    Generator that reads valid data piece-by-piece
    :param filename: path to the file to read
    :param type_cast: type required to read from file
    :param encoding: encoding used for file scanning
    :return: values on each generator iteration
    """
    with open(filename, "rt", encoding=encoding) as file:

        # scan every line
        for line in file:

            # scan every word in line
            entries = line.split()
            for entry in entries:
                # yield only correct data
                try:
                    value = type_cast(entry)
                except (TypeError, ValueError):
                    continue
                else:
                    yield value
