import algorithms


class LinkedList:
    """ Class implementing linked list structure """

    class Node:
        """ Subclass modelling a node of linked list"""

        # preventing assignment of other attributes
        __slots__ = ("prev", "next", "value")

        def __init__(self, value, prev_node=None, next_node=None):
            """
            Initializing node with links to previous and next node
            :param value: value contained inside of node of linked list
            :param prev_node: link to the previous node or None if node is first
            :param next_node: link to the next node or None is node is last
            :return:
            """

            self.value = value

            self.prev = prev_node
            self.next = next_node

        def __str__(self):
            """
            Dunder method for returning a fancy string
            :return: value inside node in string type
            """
            return str(self.value)

    def __init__(self):
        """
        Initializing empty linked list object
        :return:
        """
        self.tail = None
        self.head = None

        self.size = 0

    def __len__(self):
        """
        Dunder method returning length of linked list
        :return: number of nodes in the linked list
        """
        return self.size

    def __add__(self, other):
        """
        Dunder method overloading linked list concatenation
        :param other: list with which to concatenate
        :return: concatenated list
        """
        result = LinkedList()

        # copying current linked list
        self_ptr = self.tail
        while self_ptr:
            element = self_ptr.value
            result.append(element)
            self_ptr = self_ptr.next

        # adding other list to the resulting linked list
        other_ptr = other.tail
        while other_ptr:
            element = other_ptr.value
            result.append(element)
            other_ptr = other_ptr.next

        # result of concatenation
        return result

    def __validate_index__(self, index):
        """
        Private method for validating index and repeating avoiding
        :return: node with valid index or some Exception if invalid
        """

        # checking index type
        if not isinstance(index, int):
            raise TypeError(" linked list indices must be integers, not {type(index)}")

        # checking boundaries
        elif not -self.size <= index < self.size:
            raise IndexError(" linked list index out of range")

        # indexation and return
        else:
            # negative index is backward one
            if index < 0:
                index += self.size

            # slightly optimized indexing
            # first half = from tail
            if index < self.size // 2:
                current_node = self.tail
                current_index = 0

                # iterating until node by index is reached
                while current_index != index:
                    current_node = current_node.next
                    current_index += 1

                return current_node

            # second half = from head
            else:
                current_node = self.head
                current_index = self.size - 1

                # iterating until node by index is reached
                while current_index != index:
                    current_node = current_node.prev
                    current_index -= 1

                return current_node

    def __getitem__(self, index):
        """
        Dunder method getting the element by index (read-only)
        :param index: index of element
        :return: value of node by index
        """
        return self.__validate_index__(index).value

    def __setitem__(self, index, value):
        """
        Dunder method writing into the element by index
        :param index: index of element
        :param value: value needed to be written into the node
        :return: value of node by index
        """
        # assign a value if possible
        self.__validate_index__(index).value = value
        return

    def __delitem__(self, index):
        """
        Dunder method managing deleting indexed node
        :param index: index of element
        :return:
        """

        # use ready method for deleting nodes
        self.erase_range(index, index + 1)
        return

    def __iter__(self):
        """
        Dunder method of creating an iterator
        :return:
        """

        self.ptr = self.tail
        self.index = 0
        return self

    def __next__(self):
        """
        Dunder method of iteration
        :return: value of node or raises StopIteration if end
        """
        # checking if end is reached
        if self.ptr is None:
            raise StopIteration

        # iterating to the next element
        else:
            value = self.ptr.value
            self.ptr = self.ptr.next
            return value

    def append(self, *args):
        """
        Pushing elements to the end
        :param args: values to be appended with
        :return:
        """
        # appending values from args
        for value in args:
            # linked list is empty
            if not self.tail:
                self.head = self.tail = LinkedList.Node(value, None, None)

            # linked list is not empty
            else:
                self.head.next = LinkedList.Node(value, self.head, None)
                self.head = self.head.next

            self.size += 1
        return

    def insert(self, index, *args):
        """
        Insertion elements after some index
        :param index: index to place in
        :param args: values to be placed in
        :return:
        """

        # nothing to insert, return
        if len(args) == 0:
            return

        # insertion into the head is implemented in append method
        if index == self.size or index == -self.size - 1:
            self.append(*args)
            return

        else:
            current_node = self.__validate_index__(index)

            # insert every value we need
            for value in args:
                new_node = LinkedList.Node(value, current_node.prev, current_node)

                # if insertion is not into the tail
                if current_node.prev:
                    current_node.prev.next = new_node
                else:
                    self.tail = new_node

                # "current node" becomes next
                current_node.prev = new_node

                self.size += 1

            return

    def erase_range(self, left, right=None):
        """
        Method of erasing nodes from list
        :param left: first node to be deleted
        :param right: last node to stop deletion process
        :return:
        """

        # prepare indices
        if left < 0:
            left += self.size

        if right is None:
            right = self.size

        elif right < 0:
            right += self.size

        # assert indices for stability
        if not 0 <= left < right <= self.size:
            raise IndexError

        left_node = self.__validate_index__(left)

        right_node = None
        if right < self.size:
            right_node = self.__validate_index__(right)

        # redirect pointers to shorten list
        if right_node is not None:
            right_node.prev.next = None
            right_node.prev = left_node.prev

        else:
            self.head = left_node.prev

        if left_node.prev:
            left_node.prev.next = right_node
            left_node.prev = None
        else:
            self.tail = right_node

        # erase all remnants by garbage collector

        curr_node = left_node
        next_node = left_node.next

        while curr_node is not None:

            # erasing mutual references for deletion
            curr_node.prev = None
            curr_node.next = None

            # jump to next node to delete
            curr_node = next_node
            if next_node:
                next_node = next_node.next

            # decrease size of list
            self.size -= 1

    def pop(self, index: int = -1):
        """
        Method of deleting indexed node from list with previous return
        :param index: index of element
        :return: value that was deleted
        """
        self.erase_range(index, index + 1)
        return

    def count_uniques(self):
        """
        Method counting unique entries without changing list
        :return: count of unique entries
        """
        # trivial cases
        if self.size <= 1:
            return self.size

        # cases requiring real counting
        else:
            # sorting list
            sorted_list = algorithms.quick_sort(self)

            # counter
            # first element is already unique
            counter = 1

            # memorized previous element (to fit in one iteration)
            previous = sorted_list[0]

            # comparing element with previous and counting unique
            for element in sorted_list:
                if element != previous:
                    counter += 1
                previous = element

            # result
            return counter
