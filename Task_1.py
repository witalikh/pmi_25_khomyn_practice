def count_upward_triangles(base: int) -> int:
    """
    :param base: count of divisions of main side
    :return: count of upward triangles
    """

    # Idea: every point on i-th level can "generate" exactly (n - i) upward triangles.
    # Every i-th level has exactly i + 1 points (i = 0, ... , n)
    # So, find the sum of (n - i) * (i + 1) for i in range(0, n)

    # although, summation can be found by O(1) formula
    n = base
    return -n * (n - 1) * (n + 1) // 3 + n * n * (n + 1) // 2


# Idea for O(n): the count of downward triangle per i-th row
# is an symmetric sum with (i - 1) members
# i. e. for i = 7, sum = 1 + 2 + 3 + 3 + 2 + 1
# Solution for O(1): code in ready formulas
def count_downward_triangles(base: int) -> int:
    """
    :param base: number of triangles per side
    :return: count of upward triangles
    """

    # odd rows
    m = (base - 1) // 2 + (base - 1) % 2

    # even rows
    n = (base - 1) // 2

    # sum of upward triangles from odd and even rows
    total_of_evens = n * (n + 1) * (n + 2) // 3
    total_of_odds = (m - 1) * m * (m + 1) // 3 + m * (m + 1) // 2

    return total_of_odds + total_of_evens


def count_total_triangles(sides: int):
    """
    :param sides: number of triangles per side
    :return: total count of triangles
    """
    # Idea: count upward and downward triangles count and add them
    return count_upward_triangles(sides) + count_downward_triangles(sides)


# main running code
def main() -> None:
    """
    :return: None
    """

    greeting = """
    Задача: знайти кількість рівносторонніх трикутників
    всередині рівностороннього трикутника, якщо вздовж сторони
    можна помістити рівно n рівносторонніх трикутників
    --------------------------------------------------
    """
    print(greeting)

    n = input("Введіть число n: ")
    if n.isnumeric():
        result = count_total_triangles(int(n))
        output = "Кількість трикутників при n = " + n + " буде " + str(result)
        print(output)
    else:
        print("Некоректно введені дані, розв'язку немає :)")


if __name__ == "__main__":
    main()
