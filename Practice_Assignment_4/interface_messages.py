class InterfaceMessages:
    """ Class for Interface Messages storing """

    def __init__(self, greeting, menu_choices,
                 query_input, wrong_query,
                 exit_message,
                 list_input, list_result,
                 list_previous_output, list_output, list_size_mismatch,
                 size_input_replace, size_input_extend, wrong_size,
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

        self.size_input_replace = size_input_replace
        self.size_input_extend = size_input_extend
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

    messages = {
        "greeting":
            "Доброго дня!",

        "menu_choices":
            "Виберіть одну з доступних опцій: \n"
            "0. Вийти з програми. \n"
            "1. Показати список. \n"
            "2. Ввести власноруч список дійсних чисел. \n"
            "3. Згенерувати заново (ітератором) список випадкових дійсних чисел заданого діапазону. \n"
            "4. Догенерувати (генератором) наперед дійсні числа заданого діапазону. \n"
            "5. Додати елемент в k-тий елемент списку власноруч. \n"
            "6. Вилучити зі списку k-тий елемент.\n"
            "7. Порахувати кількість унікальних входжень в списку.",

        "query_input":
            lambda number: f"[{number}]: ",

        "wrong_query":
            "Даний запит некоректний. Будь-ласка, повторіть ще раз!",

        "exit_message":
            "Програма завершує свою роботу. До побачення!",

        "list_input":
            "Введіть елементи списку, це повинні бути дійсні числа.",

        "list_result":
            "Так виглядає утворений список:",

        "list_previous_output":
            "Так виглядає список перед модифікацією:",
        "list_output":
            "Так виглядає список після модифікації:",

        "list_size_mismatch":
            lambda missing:
            f"Деякі з введених Вами дані є записані у список. \n"
            f"Однак очікується, що Ви введете ще таку кількість коректних дійсних чисел: {missing}",

        "size_input_replace":
            "Введіть розмір списку (ціле число більше нуля), який повинен бути в результаті.",

        "size_input_extend":
            "Введіть кількість елементів (ціле число більше нуля), щоб доповнити ними список.",

        "wrong_size":
            "Введені Вами дані не може бути розмірністю списку. \n",

        "range_input":
            "Введіть два числа a, b (a <= b) - діапазон для випадково згенерованих чисел.\n",

        "wrong_range":
            "Введені Вами дані є некоректного типу або формату. \n"
            "Введіть, будь-ласка два дійсних числа a, b (a <= b)!\n",

        "index_input":
            lambda size:
            f"Введіть одне число - індекс для модифікації списку. \n"
            f"Зауваження: нумерація списку починається з одиниці, розмірність списку: {size}.",

        "wrong_index":
            lambda size:
            "Введене Вами значення є некоректного типу або формату. \n"
            f"Вводьте, будь-ласка, ціле число від 1 до {size} включно!\n",

        "element_input":
            "Введіть, будь-ласка, одне дійсне число, яке ви хочете записати в список:",

        "wrong_element":
            "Ви не ввели одне дійсне число. Будь-ласка, введіть ОДНЕ дійсне число\n",

        "deleted_output":
            lambda element:
            f"Елемент \"{element}\" успішно видалено зі списку!",

        "task_output":
            lambda uniques:
            f"Кількість унікальних елементів у зв'язаному списку дорівнює {uniques}.",

        "erase_list":
            "\nПопередження: старий список буде видалено (назавжди)!"
    }

    return InterfaceMessages(**messages)
