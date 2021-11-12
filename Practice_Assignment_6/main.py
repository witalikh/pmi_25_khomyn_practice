from menu import MainQueriesThread, prepare_messages
from observer import Observer, Event
from common import Logger


def main():
    logger = Logger("logs.txt")

    Observer("add", logger.print_to_file)
    Observer("remove", logger.print_to_file)

    Event.add_observer(Observer)

    menu_messages = prepare_messages("lang_uk.json")
    queries_thread_object = MainQueriesThread(menu_messages)
    queries_thread_object.run_thread()


if __name__ == "__main__":
    main()
