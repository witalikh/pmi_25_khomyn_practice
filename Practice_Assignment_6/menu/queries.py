from linked_list import LinkedList
from observer import Event

from menu.interface_messages import InterfaceMessages
from menu.strategies import StrategiesManager, IteratorGenStrategy, FileScanStrategy
from menu.input_manager import InputManager, ImmediateReturn


class ImmediateExit(Exception):
    """ Class for force exit """
    pass


class MainQueriesThread:
    """ Class responsible for managing main sequent queries """

    def __init__(self, messages: InterfaceMessages):
        """
        Initialize MainQueriesObject
        :param messages: object of class with strings for menu
        """
        self.linked_list = LinkedList()  # initially empty list

        self.io_manager = InputManager(messages)
        self.strategy_manager = StrategiesManager(self.io_manager)

        self.messages = messages
        self.counter = 0

    def print_list(self, message: str):
        """
        Function for fancy list printing
        :param message: message before printing list
        """
        print("\n", message, sep="")
        for counter, element in enumerate(self.linked_list):
            print(element, end=" ")
            if (counter + 1) % 10 == 0:
                print()
        print()

    def query_1(self):
        """ Choose iterator generating strategy """
        self.strategy_manager.set_strategy(IteratorGenStrategy)
        return

    def query_2(self):
        """ Choose file scan strategy """
        self.strategy_manager.set_strategy(FileScanStrategy)
        return

    def query_3(self):
        """ Input elements into list depending on chosen strategy """
        exec_outcome = self.strategy_manager.execute_strategy(self.linked_list)
        if exec_outcome:
            self.print_list(self.messages["list_output"])
        return

    def query_4(self):
        """ Delete one node k-th place """
        size = len(self.linked_list)
        if size == 0:
            return

        else:
            try:
                index = self.io_manager.input_index(1, size)

            except ImmediateReturn:
                return

            else:
                self.print_list(self.messages["list_previous_output"])
                erased = self.linked_list.pop(index)
                Event("remove", erasedList=erased, index=index, resultList=self.linked_list)

                self.print_list(self.messages["list_output"])

    def query_5(self):
        """ Delete several nodes in k-th index from list """
        size = len(self.linked_list)
        if size == 0:
            return

        else:
            try:
                a, b = self.io_manager.input_index_range(1, size)
            except ImmediateReturn:
                return
            else:

                self.print_list(self.messages["list_previous_output"])
                erased = self.linked_list.erase_range(a, b + 1)
                Event("remove", erasedList=erased, range=(a, b), resultList=self.linked_list)

                self.print_list(self.messages["list_output"])

    def query_6(self):
        """ Counting unique values and showing the result """
        result = self.linked_list.count_uniques()
        print(self.messages["task_output"].format(result))

    def query_7(self):
        """ Print list """
        self.print_list(self.messages["list_result"])

    def query_8(self):
        """ Exit """
        print(self.messages["exit_message"])
        raise ImmediateExit

    def wrong_query(self):
        """ Wrong query """
        print(self.messages["wrong_query"])

        print(self.strategy_manager.strategy)
        print(self.messages["menu_choices"])

    def process_query(self, query: str):
        """ Accept query and perform actions """
        queries = (self.query_1, self.query_2, self.query_3, self.query_4,
                   self.query_5, self.query_6, self.query_7, self.query_8)

        if query.isnumeric() and 1 <= int(query) <= len(queries):
            queries[int(query) - 1]()
        else:
            self.wrong_query()
        
    def run_thread(self):
        """ Perpetual asking queries until exit """
        print(self.strategy_manager.strategy)
        print(self.messages["menu_choices"])
        while True:

            entry = input(self.messages["query_input"].format(self.counter))
            try:
                self.process_query(entry)

            except ImmediateExit:
                return

            else:
                self.counter += 1
