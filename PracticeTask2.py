import random


class InterfaceMessages:
    """ Class for containing all interface messages """

    def __init__(self, greeting, query_input,
                 choices, wrong_choice,
                 invalid_value,
                 size_input, incorrect_size,
                 arr_input, arr_mismatch,
                 range_input,
                 arr_output, sorted_arr_output,
                 statistics_output, comparisons_output, assignments_output,
                 accesses_output, recursive_calls_output,
                 exit_msg
                 ):

        self.greeting = greeting
        self.query_input = query_input

        self.choices = choices
        self.wrong_choice = wrong_choice

        self.invalid_value = invalid_value

        self.size_input = size_input
        self.incorrect_size = incorrect_size

        self.arr_input = arr_input
        self.arr_mismatch = arr_mismatch

        self.range_input = range_input

        self.arr_output = arr_output
        self.sorted_arr_output = sorted_arr_output

        self.statistics_output = statistics_output
        self.comparisons_output = comparisons_output
        self.assignments_output = assignments_output
        self.accesses_output = accesses_output
        self.recursive_calls_output = recursive_calls_output

        self.exit = exit_msg


class Statistics:
    """ Class for collecting information about algorithm run """

    def __init__(self,
                 comparisons: int, assignments: int, accesses: int, recursive_calls: int):
        """ Initialization statistics object """
        self.comparisons = comparisons
        self.assignments = assignments
        self.accesses = accesses
        self.recursive_calls = recursive_calls


class IncorrectData(Exception):
    """ Class for invalid data exceptions """

    def __init__(self, msg):
        self.msg = msg


class ImmediateExit(Exception):
    """ Class for program's force exit """
    pass


def merge(left_half: list, left_half_size: int,
          right_half: list, right_half_size: int, compare, stats: Statistics):
    """
    Merge two iterables
    :param left_half: left half of iterable
    :param left_half_size: size of left half
    :param right_half: right half iterable
    :param right_half_size: size of right iterable
    :param compare: function(a, b) to compare a and b and sort accordingly
    :param stats: statistics object for collected about algorithm run info
    :return: merged halves of iterable
    """

    # pointers to left and right list halves to scan numbers
    left_pointer, right_pointer = 0, 0

    # pointer to result list to write in
    result_pointer = 0

    # merged list prototype
    result = [None] * (left_half_size + right_half_size)

    # both pointers haven't gone to the end of their halves
    while left_pointer < left_half_size and right_pointer < right_half_size:
        if compare(left_half[left_pointer], right_half[right_pointer]):
            result[result_pointer] = left_half[left_pointer]
            left_pointer += 1
        else:
            result[result_pointer] = right_half[right_pointer]
            right_pointer += 1

        result_pointer += 1
        if stats:
            stats.comparisons += 1  # 1 comparison
            stats.assignments += 1  # 1 write
            stats.accesses += 4  # 1 comparison = 2 accesses, 1 write = 2 accesses

    # left pointer came to sublist end
    while left_pointer < left_half_size:
        result[result_pointer] = left_half[left_pointer]
        left_pointer += 1
        result_pointer += 1

        if stats:
            stats.assignments += 1  # 1 write
            stats.accesses += 2  # 1 write = 2 accesses

    # right pointer came to sublist end
    while right_pointer < right_half_size:
        result[result_pointer] = right_half[right_pointer]
        right_pointer += 1
        result_pointer += 1

        if stats:
            stats.assignments += 1  # 1 write
            stats.accesses += 2  # 1 write = 2 accesses

    return result


# main algorithm
def merge_sort(arr: list, size: int, compare, stats: Statistics = None):
    """
    Algorithm creating sorted iterable with standard indexation
    By sorting & merging halves of it.
    :param arr: iterable with standard indexation
    :param size: size of iterable
    :param compare: function(a, b) to compare a and b and sort accordingly
    :param stats: statistics object for collected about algorithm run info
    :return: new sorted iterable
    """
    # measuring calls
    if stats:
        stats.recursive_calls += 1

    if size <= 1:
        # no need to sort, finish it
        return arr
    else:
        # split list into two halves
        middle = size // 2

        # recursively sort two halves
        left_half = merge_sort(arr[0:middle], middle, compare, stats)
        right_half = merge_sort(arr[middle: size], size - middle, compare, stats)

        # merge sorted halves and return it
        return merge(left_half, middle, right_half, size - middle, compare, stats)


def measured_merge_sort(arr: list, size: int, comparison_function):
    """
    Merge sort encapsulated and measured for comparisons and list assignments
    :param arr: iterable with standard indexation
    :param size: size of iterable
    :param comparison_function: comparison function for sorting algorithm
    :return: sorted iterable and statistics object tuple
    """

    stats = Statistics(0, 0, 0, 0)

    # return sorted list and statistics
    arr = merge_sort(arr, size, comparison_function, stats)
    return arr, stats


def validate_size(size: int, messages: InterfaceMessages):
    """
    Validates size of array and returns it validated if possible
    :param size: integer that can be size of an array
    :param messages: object containing all messages for interface output
    :return: valid size
    """
    if size <= 0:
        raise IncorrectData(messages.incorrect_size(size))

    else:
        return size


def input_size(messages: InterfaceMessages):
    """
    Function managing all details about size input process
    :param messages: object containing all messages for interface output
    :return: valid size number
    """

    print(messages.size_input)
    while True:
        size = input()
        try:
            number = validate_size(int(size), messages)

        except ValueError:
            print(messages.invalid_value(int, 1))

        except IncorrectData as instance:
            print(instance.msg)

        else:
            return number


def validate_arr(arr, size, messages: InterfaceMessages):
    """
    Validates float iterable and returns it if possible
    :param arr: iterable to be validated
    :param size: size of iterable
    :param messages: object containing all messages for interface output
    :return: validated iterable
    """

    # elements count validation
    if len(arr) != size:
        raise IncorrectData(messages.arr_mismatch)

    for elem in range(size):
        # converting strings into float if possible
        arr[elem] = float(arr[elem])

    # return valid matrix
    return arr


def input_arr(size: int, messages: InterfaceMessages):
    """
    Function managing all details about array input process
    :param size: size of future iterable
    :param messages: object containing all messages for interface output
    :return:
    """

    print(messages.arr_input)
    while True:
        # elements input (in row via space)
        arr = input().split()

        try:
            arr = validate_arr(arr, size, messages)

        except ValueError:
            print(messages.invalid_value(float, 1))

        except IncorrectData as instance:
            print(instance.msg)

        else:
            return arr


def input_and_validate_range(messages: InterfaceMessages):
    """
    Function managing all details about range input process
    :param messages: object containing all messages for interface output
    :return: tuple of valid floats
    """

    print(messages.range_input)
    while True:
        try:
            a, b = input().split()
            a, b = float(a), float(b)

        except ValueError:
            print(messages.invalid_value(float, 2))

        else:
            return a, b


def generate_arr(size: int, least: float, largest: float, precision: int):
    """
    Function creating list with random values
    :param size: size of future iterable
    :param least: lower bound of random values range
    :param largest: upper bound of random values range
    :param precision: precision for generating random values
    :return: list with random values
    """
    # array prototype
    arr = [0.] * size

    # generating random values in array
    for elem in range(size):
        arr[elem] = round(random.uniform(least, largest), precision)

    # returning ready array
    return arr


def print_arr(msg: str, arr: list, size: int):
    """
    Printing array in a fancy way
    :param msg: message to be pre-printed
    :param arr: iterable to be printed
    :param size: size of iterable
    :return:
    """
    print(msg)
    for elem in range(size):
        print(arr[elem], end=' ')
    else:
        print()


def print_stats(stats: Statistics, messages: InterfaceMessages):
    """
    Displaying all information about sorting algorithm run
    :param stats: statistics object for collected about algorithm run info
    :param messages: object containing all messages for interface output
    :return:
    """
    print(messages.statistics_output)
    print(messages.comparisons_output, stats.comparisons)
    print(messages.assignments_output, stats.assignments)
    print(messages.accesses_output, stats.accesses)
    print(messages.recursive_calls_output, stats.recursive_calls)


def do_option_1(comparison_function, messages: InterfaceMessages):
    """
    Function doing task on query 1 (input array)
    :param messages: object containing all messages for interface output
    :param comparison_function: comparison function for sorting algorithm
    :return:
    """
    size = input_size(messages)
    arr = input_arr(size, messages)

    sorted_arr, stats = measured_merge_sort(arr, size, comparison_function)

    print_arr(messages.sorted_arr_output, sorted_arr, size)
    print_stats(stats, messages)


def do_option_2(comparison_function, precision, messages: InterfaceMessages):
    """
    Function doing task on query 2 (random array)
    :param comparison_function: comparison function for sorting algorithm
    :param precision: precision for randomly generated values
    :param messages: object containing all messages for interface output
    :return:
    """
    size = input_size(messages)
    least, largest = input_and_validate_range(messages)

    arr = generate_arr(size, least, largest, precision)

    print_arr(messages.arr_output, arr, size)
    sorted_arr, stats = measured_merge_sort(arr, size, comparison_function)

    print_arr(messages.sorted_arr_output, sorted_arr, size)
    print_stats(stats, messages)


def process_queries(query, comparison_function, precision, messages: InterfaceMessages):
    """
    Function for processing all queries from main()
    :param query: query to process
    :param comparison_function: comparison function for sorting algorithm
    :param precision: precision for randomly generated values
    :param messages: object containing all messages for interface output
    :return:
    """
    if query == "1":
        do_option_1(comparison_function, messages)
    elif query == "2":
        do_option_2(comparison_function, precision, messages)
    elif query == "3":
        print(messages.exit)
        raise ImmediateExit
    else:
        print(messages.wrong_choice)
        print(messages.choices)


def menu():
    """
    Prepares all the strings into InterfaceMessages object
    :return: InterfaceMessages object
    """
    greeting = "Доброго дня!"

    def query_input(x):
        return f"[{x}]: "

    choices = "   Виберіть одну з доступних опцій:\n" \
              "1. Власноруч ввести масив розміром N і посортувати його.\n" \
              "2. Згенерувати випадково масив розміром N.\n" \
              "3. Вийти."

    wrong_choice = "Ви вибрали неіснуючу опцію або ввели некоректний формат.\n" \
                   "Спробуйте ще раз!"

    size_input = "Введіть ціле число N - розмірність масиву"

    def invalid_value(cls, count):
        x = cls
        if count == 1:
            if cls == int:
                x = "ціле число"
            elif cls == float:
                x = "дійсне число"
        elif count <= 4:
            if cls == int:
                x = f"{count} цілих числа"
            elif cls == float:
                x = f"{count} дійсних числа"
        else:
            if cls == int:
                x = f"{count} цілих чисел"
            elif cls == float:
                x = f"{count} дійсних чисел"

        return f"Вхідні дані є некоректного типу або формату.\n" \
               f"Вводьте, будь-ласка, {x}!"

    def incorrect_size(size: int):
        return f"Введене число N = {size} не може бути розмірністю масиву.\n" \
               f"Спробуйте ще раз"

    arr_input = "Введіть масив дійсних чисел через пробіл"
    arr_mismatch = "Фактична розмірність масиву не відповідає заявленій.\n" \
                   "Введіть ще раз"

    range_input = "Введіть два дійсні числа, щоб задати діапазон"

    arr_output = "Згенерований масив має такий вигляд"
    sorted_arr_output = "Відсортований масив за зростанням має такий вигляд"
    statistics_output = "Під час сортування було виміряно кількість конкретних операцій, зокрема: "

    comparisons_output = "  Кількість порівнянь дорівнює"
    assignments_output = "  Кількість присвоєнь до масиву дорівнює"
    accesses_output = "  Кількість переглядань до масиву дорівнює"
    recursive_calls_output = "  Кількість задіяних рекурсивних викликів дорівнює"

    exit_msg = "До побачення!"

    return InterfaceMessages(greeting, query_input,
                             choices, wrong_choice,
                             invalid_value,
                             size_input, incorrect_size,
                             arr_input, arr_mismatch,
                             range_input,
                             arr_output, sorted_arr_output,
                             statistics_output, comparisons_output, assignments_output,
                             accesses_output, recursive_calls_output,
                             exit_msg)


def main():
    """ Main program """

    def comparison_function(a, b):
        return a < b

    precision = 3

    messages = menu()

    print(messages.greeting)
    print(messages.choices)
    counter = 0
    while True:
        query = input(messages.query_input(counter))
        try:
            process_queries(query, comparison_function, precision, messages)
        except ImmediateExit:
            break
        else:
            counter += 1


if __name__ == "__main__":
    main()
