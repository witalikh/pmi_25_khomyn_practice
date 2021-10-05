from linked_list import LinkedList
from interface_messages import InterfaceMessages
from generators import GeneratingIterator, generate_values
from random import uniform

import validators


class ImmediateExit(Exception):
    """ Class for force exit """
    pass


class InputManager:
    """ Class responsible for automatic input and output managing"""

    def __init__(self, messages: InterfaceMessages):
        """
        Initializes Input-Output Manager
        :param messages: object of messages
        """
        self.messages = messages

    def input_size(self, message):
        """
        Function managing size input details
        :return: valid size
        """

        print(message)
        while True:
            size = input()
            try:
                validated_size = validators.validate_integer(size, 1)
            except (TypeError, ValueError, AssertionError):
                print(self.messages.wrong_size)
            else:
                return validated_size

    def input_range(self):
        """
        Function managing range input details
        :return: valid tuple that is a range
        """

        print(self.messages.range_input)
        while True:
            nums = input().split()
            try:
                range_of_floats = validators.validate_range(*nums)
            except (TypeError, ValueError):
                print(self.messages.wrong_range)
            else:
                return range_of_floats

    def input_list(self, size: int):
        """
        Function managing list elements input
        :param size: size to be supposed in list
        :return: valid list of values
        """

        print(self.messages.list_input)
        required_size = size
        result = LinkedList()
        while True:
            result.input(required_size)
            result = validators.validate_iterable_values(result, float)
            try:
                if size:
                    validators.validate_iterable_size(result, size)
            except AssertionError:
                required_size = size - len(result)
                print(self.messages.list_size_mismatch(required_size))
            else:
                return result

    def input_index(self, size: int):
        """
        Function managing index input
        :param size: size of list
        :return: valid index
        """

        print(self.messages.index_input(size))
        while True:
            entry = input()
            try:
                index = validators.validate_integer(entry, 1, size)
            except (TypeError, ValueError):
                print(self.messages.wrong_index(size))
            else:
                return index

    def input_element(self):
        """
        Function managing input a single float number
        :return: valid float
        """
        print(self.messages.element_input)
        while True:
            entry = input()
            try:
                value = validators.validate_float(entry)
            except (TypeError, ValueError):
                print(self.messages.wrong_element)
            else:
                return value


class QueriesThread:
    """ Class responsible for managing sequent queries """

    def __init__(self, messages: InterfaceMessages):
        """

        :param messages: object of class with strings for menu
        """
        self.linked_list = LinkedList()  # initially empty list
        self.random_source = lambda x, y: round(uniform(x, y), 3)

        self.io_manager = InputManager(messages)
        self.messages = messages

        self.counter = 0

    def print_list(self, message: str):
        """
        Function for fancy list printing
        :param message: message before printing list
        :return:
        """

        print("\n", message, sep="")
        for counter, element in enumerate(self.linked_list):
            print(element, end=" ")
            if (counter + 1) % 10 == 0:
                print()
        print()

    def erase_list_warning(self):
        """
        Helper method for printing list before total erase
        :return:
        """
        if len(self.linked_list):
            self.print_list(self.messages.erase_list)
        print()

    def query_0(self):
        """
        Exit
        """
        print(self.messages.exit_message)
        raise ImmediateExit

    def query_1(self):
        """
        Printing list
        """
        self.print_list(self.messages.list_result)

    def query_2(self):
        """
        Managing manual list input
        """

        self.erase_list_warning()

        size = self.io_manager.input_size(self.messages.size_input_replace)
        self.linked_list = self.io_manager.input_list(size)

        self.print_list(self.messages.list_result)

    def query_3(self):
        """
        Generating random list via iterator and overwrite initial list
        """

        self.erase_list_warning()

        size = self.io_manager.input_size(self.messages.size_input_replace)
        range_of_floats = self.io_manager.input_range()

        result = LinkedList()
        iterator = GeneratingIterator(size, *range_of_floats, default_source=self.random_source)

        # iter_obj = iter(iterator)
        # for i in range(size):
        #    result.append(next(iterator))
        result.extend(iterator)

        self.linked_list = result
        self.print_list(self.messages.list_result)

    def query_4(self):
        """
        Generating random list via yield-generator and extend it
        """

        size = self.io_manager.input_size(self.messages.size_input_extend)
        range_of_floats = self.io_manager.input_range()

        gen_obj = generate_values(size, *range_of_floats, default_source=self.random_source)

        self.linked_list.extend(gen_obj)
        self.print_list(self.messages.list_output)

    def query_5(self):
        """
        Insert a node into k-th place
        :return:
        """
        size = len(self.linked_list)

        index = self.io_manager.input_index(size + 1)
        element = self.io_manager.input_element()

        self.print_list(self.messages.list_previous_output)

        self.linked_list.insert(index - 1, element)
        self.print_list(self.messages.list_output)

    def query_6(self):
        """
        Delete some node in k-th index from list
        :return:
        """
        size = len(self.linked_list)

        index = self.io_manager.input_index(size)

        self.print_list(self.messages.list_previous_output)
        deleted_value = self.linked_list.pop(index - 1)

        print(self.messages.deleted_output(deleted_value))
        self.print_list(self.messages.list_output)

    def query_7(self):
        """
        Counting unique values and showing the result
        :return:
        """
        result = self.linked_list.count_uniques()
        print(self.messages.task_output(result))

    def wrong_query(self):
        """
        Wrong query sent
        :return:
        """
        print(self.messages.wrong_query, "\n", self.messages.menu_choices)

    def process_query(self, query: int):
        """
        Accepting query and performing actions
        :param query: query to process
        :return: actions
        """
        queries = (self.query_0, self.query_1, self.query_2, self.query_3,
                   self.query_4, self.query_5, self.query_6, self.query_7,
                   self.wrong_query)

        if 0 <= query < len(queries) - 1:
            queries[query]()
        else:
            queries[-1]()
        
    def run_thread(self):
        """
        Perpetual asking queries until exit
        :return:
        """
        print(self.messages.menu_choices)
        while True:
            entry = input(self.messages.query_input(self.counter))
            try:
                query = int(entry)
                self.process_query(query)
            except (ValueError, TypeError):
                print(self.messages.wrong_query)
            except ImmediateExit:
                return
            else:
                self.counter += 1
