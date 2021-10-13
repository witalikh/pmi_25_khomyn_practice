from interface_messages import InterfaceMessages
import validators


class ImmediateReturn(Exception):
    pass


class InputManager:
    """ Automatic input and output managing"""

    def __init__(self, messages: InterfaceMessages):
        """
        Initializes Input Manager
        :param messages: object of messages
        """
        self.messages = messages

    def input_size(self):
        """
        Function managing size input details
        :return: valid size
        """

        print(self.messages.size_input)
        size = input()

        try:
            validated_size = validators.validate_value(int, size, 1)

        except (TypeError, ValueError, AssertionError):
            print(self.messages.wrong_size)
            raise ImmediateReturn

        else:
            return validated_size

    def input_range(self):
        """
        Function managing range input details
        :return: valid tuple that is a range of floats
        """

        print(self.messages.range_input)
        nums = input().split()

        try:
            range_of_floats = validators.validate_range(float, *nums)

        except (TypeError, ValueError):
            print(self.messages.wrong_range)
            raise ImmediateReturn

        else:
            return range_of_floats

    def input_index(self, start: int, end: int):
        """
        Function managing index input
        :param start: starting index
        :param end: ending index
        :return: valid index
        """

        # no way to choose something else, inform and return
        if start == end:
            print(self.messages.automatic_index_warning)
            return 0

        print(self.messages.index_input(start, end))
        entry = input()

        try:
            index = validators.validate_value(int, entry, start, end)

        except (TypeError, ValueError):
            print(self.messages.wrong_index(start, end))
            raise ImmediateReturn

        else:
            return index - start

    def input_index_range(self, start: int, end: int):
        """
        Function managing two indices input
        :param start: starting index
        :param end: ending index
        :return: valid pair of indices
        """

        print(self.messages.index_range_input(start, end))
        range_of_ints = input().split()

        try:
            a, b = validators.validate_range(int, *range_of_ints,
                                             lower_bound=start, upper_bound=end)

        except (TypeError, ValueError):
            print(self.messages.wrong_index_range(start, end))
            raise ImmediateReturn

        else:
            return a - start, b - start

    def input_file_path(self):
        """
        Function managing input a file path
        :return: valid file path
        """

        entry = input(self.messages.file_path_input)

        try:
            path = validators.validate_file_path(entry)

        except FileNotFoundError:
            print(self.messages.wrong_file_path)
            raise ImmediateReturn

        else:
            return path
