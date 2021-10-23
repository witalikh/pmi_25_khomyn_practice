from abc import ABC, abstractmethod

from linked_list import LinkedList
from input_manager import InputManager, ImmediateReturn

from generators import GeneratingIterator, scan_from_file

from random import uniform


class Strategy(ABC):
    """
    Abstract base class for strategies of filling the list
    """

    def __init__(self, input_manager: InputManager):
        """
        Initializing subclasses is uniform
        :param input_manager: object that manages fields input
        """
        self.input_manager = input_manager
        self.messages = self.input_manager.messages

    @abstractmethod
    def execute(self, iterable: LinkedList):
        """
        Abstract method, to override in subclasses
        :param iterable: iterable to work with
        :return: True if strategy eas done successfully
        """
        pass


class IteratorGenStrategy(Strategy):
    """
    Class-strategy for filling iterables with random values
    """

    def __str__(self):
        """
        Dunder method of fancy string
        :return: fancy string of strategy
        """
        return self.messages.first_strategy_chosen

    def execute(self, iterable: LinkedList):
        """
        Execute strategy: fill iterable with random values (parameters asked)
        :param iterable: iterable to modify
        :return: True if strategy eas done successfully
        """
        try:
            size = self.input_manager.input_size()
            range_of_floats = self.input_manager.input_range()
            index = self.input_manager.input_index(1, len(iterable) + 1)

        except ImmediateReturn:
            return False

        else:
            def source(x, y):
                return round(uniform(x, y), 3)

            gen_iter = GeneratingIterator(size, *range_of_floats, default_source=source)
            iterable.insert(index, *gen_iter)

            return True


class FileScanStrategy(Strategy):
    """
    Class-strategy for scanning floats from file into iterable
    """

    def __str__(self):
        """
        Dunder method of fancy string
        :return: fancy string of strategy
        """
        return self.messages.second_strategy_chosen

    def execute(self, iterable: LinkedList):
        """
        Execute strategy: ask for filename and start index to fill the iterable
        :param iterable: iterable to modify
        :return: True if strategy eas done successfully
        """
        try:
            file_path = self.input_manager.input_file_path()
            index = self.input_manager.input_index(1, len(iterable) + 1)

        except ImmediateReturn:
            return False

        else:
            iterable.insert(index, *scan_from_file(file_path, float))
            return True


class DefaultStrategy(Strategy):

    def __str__(self):
        """
        Dunder method of fancy string
        :return: fancy string of strategy
        """
        return self.messages.empty_strategy

    def execute(self, iterable):
        """
        Execute strategy: warn user that no strategy is chosen
        :param iterable: iterable to modify
        :return: True if strategy eas done successfully
        """
        print(self)
        return False


class StrategiesManager:
    """
    Class that manages the strategies of appending iterable
    """

    strategy: Strategy

    def __init__(self, input_manager: InputManager):
        """
        Initializes strategies context with input manager and sets default strategy
        :param input_manager: object that manages fields input
        """
        self.input_manager = input_manager
        self.strategy = DefaultStrategy(input_manager)

    def set_strategy(self, strategy=None):
        """
        Establish concrete strategy
        :param strategy: strategy of appending iterable
        :return:
        """
        if strategy is not None:
            self.strategy = strategy(self.input_manager)

        else:
            self.strategy = DefaultStrategy(self.input_manager)

        print(self.strategy)

    def execute_strategy(self, iterable):
        """
        Execute strategy: modify the iterable accordingly
        :param iterable: iterable to modify
        :return:
        """
        return self.strategy.execute(iterable)
