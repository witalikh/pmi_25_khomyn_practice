from common import algorithms


class LinkedList:
    """ Class implementing linked list structure """

    class Node:
        """ Subclass modelling a node of linked list"""

        # preventing assignment of other attributes
        __slots__ = ("prev", "next", "value")

        def __init__(self, value, prev_node=None, next_node=None):
            """ Initializer: links between nodes and value"""

            self.value = value

            self.prev = prev_node
            self.next = next_node

        def __str__(self):
            """
            :return: value inside node in string type
            """
            return str(self.value)

    def __init__(self, *args):
        """
        Initializer: linked list object
        """
        self.__tail: (LinkedList.Node, None) = None
        self.__head: (LinkedList.Node, None) = None

        self.__size = 0
        self.append(*args)

    def __del__(self):
        """
        Destructor: delete all nodes with garbage collector
        """

        if self.__size > 0:

            curr_node = self.__tail
            next_node = self.__tail.next

            while curr_node is not None:

                curr_node.prev = None
                curr_node.next = None

                curr_node = next_node
                if next_node:
                    next_node = next_node.next

            return

    def __len__(self):
        """
        Dunder method returning length of linked list
        :return: number of nodes in the linked list
        """
        return self.__size

    def __str__(self):
        """
        :return: fancy string of linked list
        """
        curr_node = self.__tail
        result = "["
        while curr_node is not None:
            result = result + str(curr_node.value)
            curr_node = curr_node.next
            if curr_node is not None:
                result = result + ", "
        return result + "]"

    def __add__(self, other):
        """
        Linked list concatenation
        :param other: list with which to concatenate
        :return: concatenated list
        """
        result = LinkedList()

        # copying current linked list
        self_ptr = self.__tail
        while self_ptr:
            element = self_ptr.value
            result.append(element)
            self_ptr = self_ptr.next

        # adding other list to the resulting linked list
        other_ptr = other.__tail
        while other_ptr:
            element = other_ptr.value
            result.append(element)
            other_ptr = other_ptr.next

        # result of concatenation
        return result

    def __validate_index__(self, index):
        """
        Private method: index validation
        :return: node onto a valid index
        :raise: TypeError when non-integer, IndexError when integer is not an index
        """

        if not isinstance(index, int):
            raise TypeError(" linked list indices must be integers, not {type(index)}")

        elif not -self.__size <= index < self.__size:
            raise IndexError(" linked list index out of range")

        else:
            # backward indices rewriting
            if index < 0:
                index += self.__size

            # node closer to first half
            if index < self.__size // 2:
                current_node = self.__tail
                current_index = 0

                while current_index != index:
                    current_node = current_node.next
                    current_index += 1

                return current_node

            # node closer to second half
            else:
                current_node = self.__head
                current_index = self.__size - 1

                while current_index != index:
                    current_node = current_node.prev
                    current_index -= 1

                return current_node

    def __getitem__(self, index):
        """
        Get the element by index for reading
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
        self.erase_range(index, index + 1)
        return

    def __iter__(self):
        """
        Linked list iterator: two additional attributes given
        :return: linked list iterator object
        """
        self.ptr = self.__tail
        self.index = 0
        return self

    def __next__(self):
        """
        Forward iteration
        :return: value of current node
        :raise: StopIteration when end
        """
        if self.ptr is None:
            raise StopIteration

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
            if not self.__tail:
                self.__head = self.__tail = LinkedList.Node(value, None, None)

            # linked list is not empty
            else:
                self.__head.next = LinkedList.Node(value, self.__head, None)
                self.__head = self.__head.next

            self.__size += 1
        return

    def insert(self, index, *args):
        """
        Insertion elements after some index
        :param index: index to place in
        :param args: values to be placed in
        """
        if len(args) == 0:
            return

        if index == self.__size or index == -self.__size - 1:
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
                    self.__tail = new_node

                # "current node" becomes next
                current_node.prev = new_node

                self.__size += 1

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
            left += self.__size

        if right is None:
            right = self.__size

        elif right < 0:
            right += self.__size

        # assert indices for stability
        if not 0 <= left < right <= self.__size:
            raise IndexError

        left_node = self.__validate_index__(left)

        right_node = None
        if right < self.__size:
            right_node = self.__validate_index__(right)

        size = right - left
        result = LinkedList()

        if right_node is not None:
            right_node.prev.next = None
            result.__head = right_node.prev
            right_node.prev = left_node.prev

        else:
            result.__head = self.__head
            self.__head = left_node.prev

        if left_node.prev:
            left_node.prev.next = right_node
            left_node.prev = None
        else:
            self.__tail = right_node

        result.__tail = left_node

        self.__size -= size
        result.__size = size

        return result

    def pop(self, index: int = -1):
        """
        Method of deleting indexed node from list with previous return
        :param index: index of element
        :return: value that was deleted
        """
        return self.erase_range(index, index + 1)

    def count_uniques(self):
        """
        Counting unique entries without changing list
        :return: count of unique entries
        """
        if self.__size <= 1:
            return self.__size

        else:
            sorted_list = algorithms.quick_sort(self)
            counter = 1

            previous = sorted_list[0]

            for element in sorted_list:
                if element != previous:
                    counter += 1
                previous = element

            return counter
