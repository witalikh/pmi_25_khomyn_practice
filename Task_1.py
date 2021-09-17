class ImmediateExit(Exception):
    """Custom class for breaking program"""
    pass


def count_upward_triangles(base: int) -> int:
    """
    Function that counts upward-oriented triangles
    :param base: count of divisions of main side
    :return: count of upward triangles
    """

    # Idea: every point on i-th level can "generate" exactly (n - i) upward triangles.
    # Every i-th level has exactly i + 1 points (i = 0, ... , n)
    # So, find the sum of (n - i) * (i + 1) for i in range(0, n)

    # although, summation can be found by O(1) formula
    n = base
    return n * n * (n + 1) // 2 - n * (n - 1) * (n + 1) // 3


# Idea for O(n): the count of downward triangle per i-th row
# is an symmetric sum with (i - 1) members
# e. g. for i = 7, sum = 1 + 2 + 3 + 3 + 2 + 1
# Solution for O(1): code in ready formulas
def count_downward_triangles(base: int) -> int:
    """
    Function that counts downward-oriented triangles
    :param base: number of triangles per side
    :return: count of upward triangles
    """

    # odd rows of triangles base
    m = (base - 1) // 2 + (base - 1) % 2

    # even rows of triangles base
    n = (base - 1) // 2

    # count of upward triangles from odd and even rows
    total_of_evens = n * (n + 1) * (n + 2) // 3
    total_of_odds = (m - 1) * m * (m + 1) // 3 + m * (m + 1) // 2

    # total count of upward triangles
    return total_of_odds + total_of_evens


# main algorithm function
def count_total_triangles(sides: int):
    """
    Function counting triangles inside big equilateral triangle
    :param sides: number of triangles per side
    :return: total count of triangles
    """
    # count upward and downward triangles count and add them
    return count_upward_triangles(sides) + count_downward_triangles(sides)


# validation of input of required type
def try_to_input(required_type, input_msg, wrong_input_msg, stop_words):
    """
    Function intercepting input and requiring it until correct data is written
    :param required_type: the type that input data should convert from str
    :param input_msg: message printed while input
    :param wrong_input_msg: message warning about incorrect data before asking again
    :param stop_words: special words (case-independent) to force exit
    :return: output value in case of success
    """
    while True:
        entry = input(input_msg)

        # if program is needed to be closed beforehand
        # sorry for fancy method below, it's additional functionality
        if entry.lower() in stop_words:
            raise ImmediateExit

        try:
            # convert to the type
            output = required_type(entry)

        except ValueError:
            # type is incompatible
            print(wrong_input_msg)
            continue

        else:
            # type is compatible
            return output


def input_manage(greeting_msg,
                 input_msg,
                 wrong_format_msg, wrong_value_msg,
                 stop_words):
    """
    Function intercepting input details
    :param greeting_msg:
    :param input_msg:
    :param wrong_format_msg:
    :param wrong_value_msg:
    :param stop_words:
    :return:
    """
    print(greeting_msg, input_msg, sep='\n')
    output = try_to_input(int, "n = ", wrong_format_msg, stop_words)

    # (notice: triangle with 0 triangles inside is considered as point)
    if output < 0:
        print(wrong_value_msg)
        raise ImmediateExit

    else:
        return output


# main running code
def main() -> None:
    """
    :return: None
    """

    greeting_msg = """
    Задача: знайти кількість рівносторонніх трикутників
    всередині рівностороннього трикутника, якщо вздовж сторони
    можна помістити рівно n рівносторонніх трикутників
    """

    input_msg = """
    Введіть число n для обчислення результату
    Або EXIT в довільному регістрі для виходу"""

    wrong_format_msg = """
    Введене значення некоректне за форматом. Спробуйте ще раз!"""

    wrong_value_msg = """Для даного числа не існує розв'язку задачі: функція обчислення на ній не визначена"""

    stop_words = ["exit"]

    exit_msg = """Програма передчасно завершила роботу, дякую за увагу!"""

    output_msg = "Максимальна кількість трикутників, " \
                 "які можна знайти в даному рівносторонньому, дорівнює"

    try:
        # evaluate an input
        n = input_manage(greeting_msg,
                         input_msg,
                         wrong_format_msg,wrong_value_msg,
                         stop_words)

    except ImmediateExit:
        # print a farewell
        print(exit_msg)

    else:
        # find a solution and represent it
        # possibly to encapsulate into function, but insensible
        print(output_msg, count_total_triangles(n))


if __name__ == "__main__":
    main()
