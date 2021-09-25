from linked_list import LinkedList
from interface_messages import InterfaceMessages

import validators
import random


class ImmediateExit(Exception):
    """ Class for force exit """
    pass


class InputOutputManager:
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
                pass
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
    
    @staticmethod
    def print_list(linked_list: LinkedList, message: str):
        """
        Function for fancy list printing
        :param linked_list: list to be printed
        :param message: message before printing list
        :return:
        """

        print()
        print(message)
        counter = 0
        for element in linked_list:
            print(element, end="\t")
            counter += 1
            if counter == 10:
                print()
                counter = 0
        print()


class QueriesThread:
    """ Class responsible for managing sequent queries """

    def __init__(self, messages: InterfaceMessages):
        """

        :param messages: object of class with strings for menu
        """
        self.linked_list = LinkedList()  # initially empty list
        
        self.io_manager = InputOutputManager(messages)
        self.messages = messages

        self.counter = 0

    def erase_list_warning(self):
        """
        Helper method for erasing list
        :return:
        """
        if len(self.linked_list):
            self.io_manager.print_list(self.linked_list, self.messages.erase_list)
        print()

    def fulfil_query_1(self):
        """
        Managing manual list input
        :return:
        """

        self.erase_list_warning()

        size = self.io_manager.input_size()
        self.linked_list = self.io_manager.input_list(size)

        self.io_manager.print_list(self.linked_list, self.messages.list_result)

    def fulfil_query_2(self):
        """
        Generating random list
        :return:
        """

        self.erase_list_warning()

        size = self.io_manager.input_size()
        range_of_floats = self.io_manager.input_range()
        result = LinkedList()

        def generator(x, y):
            return round(random.uniform(x, y), 3)

        result.generate_next(size, generator, *range_of_floats)
        self.linked_list = result

        self.io_manager.print_list(self.linked_list, self.messages.list_result)

    def fulfil_query_3(self):
        """
        Insert a node into k-th place
        :return:
        """
        linked_list = self.linked_list
        size = len(linked_list)

        index = self.io_manager.input_index(size)
        element = self.io_manager.input_element()

        self.io_manager.print_list(linked_list, self.messages.list_previous_output)

        linked_list.insert(index, element)
        self.io_manager.print_list(linked_list, self.messages.list_output)

    def fulfil_query_4(self):
        """
        Delete some node in k-th index from list
        :return:
        """
        linked_list = self.linked_list
        size = len(linked_list)

        index = self.io_manager.input_index(size)

        self.io_manager.print_list(linked_list, self.messages.list_previous_output)
        deleted_value = linked_list.pop(index - 1)

        # suspiciously hard code
        print(self.messages.deleted_output(deleted_value))
        self.io_manager.print_list(linked_list, self.messages.list_output)

    def fulfil_query_5(self):
        """
        Counting unique values and showing the result
        :return:
        """
        result = self.linked_list.count_uniques()
        print(self.messages.task_output(result))

    def process_query(self, query: int):
        """
        Accepting query and performing actions
        :param query: query to process
        :return: actions
        """
        if query == 0:
            self.io_manager.print_list(
                self.linked_list, self.messages.list_result)
            return
        elif query == 1:
            self.fulfil_query_1()
            return
        elif query == 2:
            self.fulfil_query_2()
            return
        elif query == 3:
            self.fulfil_query_3()
            return
        elif query == 4:
            self.fulfil_query_4()
            return
        elif query == 5:
            self.fulfil_query_5()
            return
        elif query == 6:
            print(self.messages.exit_message)
            raise ImmediateExit
        else:
            print(self.messages.wrong_query)
            print()
            print(self.messages.menu_choices)
        
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
