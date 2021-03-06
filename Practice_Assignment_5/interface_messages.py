class InterfaceMessages:
    """ Class for Interface Messages storing """

    def __init__(self, **kwargs):
        """
        Initializes InterfaceMessages object for convenience
        """
        for key, value in kwargs.items():
            self.__setattr__(key, value)


def prepare_messages():
    """
    Function with prepared ukrainian messages
    :return:
    """

    messages = {
        "menu_choices":
            "Виберіть одну з доступних опцій: \n"
            "1. Використати стратегію 1 (генерація елементів) для вставки у список. \n"
            "2. Використати стратегію 2 (зчитування з файлу) для вставки у список. \n"
            "3. Генерувати дані.\n"
            "4. Видалити елемент за вказаною позицією. \n"
            "5. Видалити декілька елементів в межах початкової та кінцевої позиції.\n"
            "6. Порахувати кількість унікальних входжень в списку. \n"
            "7. Вивести список. \n"
            "8. Вихід. \n",

        "query_input":
            lambda number: f"[{number}]: ",

        "wrong_query":
            "Даний запит некоректний. Будь-ласка, повторіть ще раз!\n",

        "exit_message":
            "Програма завершує свою роботу. До побачення!",

        "first_strategy_chosen":
            "Вибрано стратегію генерації випадкових дійсних чисел",

        "second_strategy_chosen":
            "Вибрано стратегію зчитування даних з файлу",

        "empty_strategy":
            "Ви поки що не вибрали жодної стратегії. Виберіть спочатку її, будь-ласка.",

        "list_result":
            "Так виглядає утворений список:",

        "list_previous_output":
            "Так виглядає список перед модифікацією:",

        "list_output":
            "Так виглядає список після модифікації:",

        "size_input":
            "Введіть розмір списку (ціле число більше нуля), який ви хочете ввести в результуючий.",

        "wrong_size":
            "Введені Вами дані не можуть бути розмірністю списку. \n",

        "range_input":
            "Введіть два числа a, b (a <= b) - діапазон для випадково згенерованих чисел.",

        "wrong_range":
            "Введені Вами дані є некоректного типу або формату. \n"
            "Введіть, будь-ласка два дійсних числа a, b (a <= b)!\n",

        "automatic_index_warning":
            "Список порожній, заповнюємо з початку списку",

        "index_input":
            lambda start, end:
            f"Введіть одне число - індекс для модифікації списку. \n"
            f"Зауваження: нумерація списку починається з {start} і закінчується {end}.",

        "wrong_index":
            lambda start, end:
            f"Введене Вами значення є некоректного типу або формату. \n"
            f"Вводьте, будь-ласка, ціле число від {start} до {end} включно!\n",

        "index_range_input":
            lambda start, end:
            f"Введіть два числа a, b (a <= b) - індекси для модифікації списку (видалення). \n"
            f"Зауваження: нумерація списку починається з {start} і закінчується {end}.",

        "wrong_index_range":
            lambda start, end:
            f"Введені Вами значення є некоректного типу або формату. \n"
            f"Введіть, будь-ласка, два цілих числа a, b (a <= b) від {start} до {end} включно!\n",


        "element_input":
            "Введіть, будь-ласка, одне дійсне число, яке ви хочете записати в список:",

        "wrong_element":
            "Ви не ввели одне дійсне число. Будь-ласка, введіть ОДНЕ дійсне число\n",

        "file_path_input":
            "Введіть назву файлу або шлях до файлу: ",

        "wrong_file_path":
            "Введемий Вами шлях файлу некоректний. Спробуйте ще раз! \n",

        "deleted_output":
            "Елемент успішно видалено зі списку!",

        "task_output":
            lambda uniques:
            f"Кількість унікальних елементів у зв'язаному списку дорівнює {uniques}.",

    }

    return InterfaceMessages(**messages)
