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

    def input_size(self):
        """
        Function managing size input details
        :return: valid size
        """

        print(self.messages.size_input)
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
        Function managing linked list elements input
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


class MainQueriesThread:
    """ Class responsible for managing main sequent queries """

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

    def side_menu_choice(self, message, *args):
        """
        Helper method for side menu choices
        :param message: message to print
        :param args: choices to choose
        :return: choice from args
        """
        while True:
            try:
                query = int(input(message))
            except ValueError:
                print(self.messages.wrong_query)
            else:
                if 0 <= query < len(args):
                    return args[query]
                else:
                    print(self.messages.wrong_query)

    def erase_list_process_choice(self):
        """
        Helper method for printing list before total erase and total erase if needed
        :return:
        """
        # asking whether preserve list
        list_action = self.side_menu_choice(self.messages.list_preservation_choices,
                                            None, 1, 2)

        # exit immediately with no action
        if not list_action:
            return False

        # erase list if necessary
        elif list_action == 1:
            # warn user about that
            if len(self.linked_list):
                self.print_list(self.messages.erase_list)

            self.linked_list = LinkedList()

        return True

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
        Managing manual list input and overwrite or extend initial list
        """

        outcome = self.erase_list_process_choice()
        if not outcome:
            return

        size = self.io_manager.input_size()
        self.linked_list.extend(self.io_manager.input_list(size))

        self.print_list(self.messages.list_result)

    def query_3(self):
        """
        Generating random list and overwrite or extend initial list
        """
        outcome = self.erase_list_process_choice()
        if not outcome:
            return

        # ask for generating way
        generating_way = self.side_menu_choice(self.messages.generator_choices,
                                               None, GeneratingIterator, generate_values)

        if generating_way:
            # input values
            size = self.io_manager.input_size()
            range_of_floats = self.io_manager.input_range()

            # iterator and generator are uniform signatures and behaviour
            generating_object = generating_way(size, *range_of_floats, default_source=self.random_source)

            self.linked_list.extend(generating_object)
            self.print_list(self.messages.list_result)

    def query_4(self):
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

    def query_5(self):
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

    def query_6(self):
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
        print(self.messages.wrong_query, "\n", self.messages.menu_choices, sep='')

    def process_query(self, query: int):
        """
        Accepting query and performing actions
        :param query: query to process
        :return: actions
        """
        queries = (self.query_0, self.query_1, self.query_2, self.query_3,
                   self.query_4, self.query_5, self.query_6,
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
