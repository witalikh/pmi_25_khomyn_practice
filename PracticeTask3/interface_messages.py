class InterfaceMessages:
    """ Class for Interface Messages storing """

    def __init__(self, greeting, menu_choices,
                 query_input, wrong_query,
                 exit_message,
                 list_input, list_result,
                 list_previous_output, list_output, list_size_mismatch,
                 size_input, wrong_size,
                 range_input, wrong_range,
                 index_input, wrong_index,
                 element_input, wrong_element,
                 deleted_output,
                 task_output, erase_list
                 ):
        """
        Initializes InterfaceMessages object for convenience
        """
        self.greeting = greeting
        self.menu_choices = menu_choices

        self.query_input = query_input
        self.wrong_query = wrong_query
        self.exit_message = exit_message

        self.list_input = list_input
        self.list_result = list_result
        self.list_previous_output = list_previous_output
        self.list_output = list_output
        self.list_size_mismatch = list_size_mismatch

        self.size_input = size_input
        self.wrong_size = wrong_size

        self.range_input = range_input
        self.wrong_range = wrong_range

        self.index_input = index_input
        self.wrong_index = wrong_index

        self.element_input = element_input
        self.wrong_element = wrong_element

        self.deleted_output = deleted_output
        self.task_output = task_output

        self.erase_list = erase_list


def prepare_messages():
    """
    Function with prepared ukrainian messages
    :return:
    """

    greeting = "Доброго дня!"

    menu_choices = "Виберіть одну з доступних опцій: \n" \
                   "0. Показати список. \n" \
                   "1. Ввести власноруч список дійсних чисел. \n" \
                   "2. Згенерувати список випадкових дійсних чисел заданого діапазону. \n" \
                   "3. Додати елемент в k-тий елемент списку власноруч. \n" \
                   "4. Вилучити зі списку k-тий елемент.\n" \
                   "5. Порахувати кількість унікальних входжень в списку. \n" \
                   "6. Вийти з програми."

    def query_input(number: int):
        return f"[{number}]: "

    wrong_query = "\nДаний запит некоректний. Будь-ласка, повторіть ще раз!"

    exit_message = "Програма завершує свою роботу. До побачення!"

    list_input = "Введіть елементи списку, це повинні бути дійсні числа. \n" \
                 "Попередження: некоректні дані в потоці ігноруватимуться і відфільтруються"

    list_result = "Так виглядає утворений список:"

    list_previous_output = "Так виглядає список перед модифікацією:"
    list_output = "Так виглядає список після модифікації:"

    def list_size_mismatch(missing: int):
        return f"\nДеякі з введених Вами дані є записані у список. \n" \
               f"Однак очікується, що Ви введете ще таку кількість коректних дійсних чисел: {missing}"

    size_input = "Введіть розмір списку (ціле число більше нуля), який повинен бути в результаті.\n" \
                 "Попередження: некоректний тип або формат сприйматись не буде!"

    wrong_size = "\nВведені Вами дані не може бути розмірністю списку. \n" \
                 "Спробуйте ще раз, ввівши додатнє ціле число!"

    range_input = "Введіть два числа a, b (a <= b) - діапазон для випадково згенерованих чисел.\n" \
                  "Зауваження: некоректні типи або формати не сприйматимуться!"

    wrong_range = "\nВведені Вами дані є некоректного типу або формату. \n" \
                  "Введіть, будь-ласка два дійсних числа a, b (a <= b)!"

    def index_input(size: int):
        return f"Введіть одне число - індекс для модифікації списку. \n" \
               f"Зауваження: нумерація списку починається з одиниці, розмірність списку: {size}.\n" \
               f"Некоректний тип чи формат або некоректне число не сприйматимуться!"

    def wrong_index(size: int):
        return f"\nВведене Вами значення є некоректного типу або формату. \n" \
               f"Вводьте, будь-ласка, ціле число від 1 до {size} включно!"

    element_input = "Введіть, будь-ласка, одне дійсне число, яке ви хочете записати в список:"

    wrong_element = "\nВи не ввели одне дійсне число. Будь-ласка, введіть ОДНЕ дійсне число"

    def deleted_output(element: float):
        return f"Елемент \"{element}\" успішно видалено зі списку!"

    def task_output(uniques: int):
        return f"Кількість унікальних елементів у зв'язаному списку дорівнює {uniques}."

    erase_list = "\nПопередження: старий список буде видалено (назавжди)!"

    return InterfaceMessages(greeting, menu_choices,
                             query_input, wrong_query,
                             exit_message,
                             list_input, list_result,
                             list_previous_output, list_output, list_size_mismatch,
                             size_input, wrong_size,
                             range_input, wrong_range,
                             index_input, wrong_index,
                             element_input, wrong_element,
                             deleted_output,
                             task_output,
                             erase_list)
