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


def generate_values(count: int, *args, default_source=random.uniform, **kwargs):
    """
    Generator function for generating random values
    :param count: how many values to generate
    :param args: arguments to source function
    :param default_source:
    :param kwargs: keyword arguments to source function
    :return:
    """

    index: int = 0
    while index < count:

        # return intermediately generated value and wait next() call
        yield default_source(*args, **kwargs)
        index += 1
