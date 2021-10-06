from interface_messages import prepare_messages
from queries import MainQueriesThread


def main():
    menu_messages = prepare_messages()
    queries_thread_object = MainQueriesThread(menu_messages)
    queries_thread_object.run_thread()


if __name__ == "__main__":
    main()
