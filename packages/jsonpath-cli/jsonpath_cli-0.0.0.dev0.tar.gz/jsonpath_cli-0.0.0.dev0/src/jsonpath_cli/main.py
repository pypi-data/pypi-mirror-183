from jsonpath_cli._my_argument_parser import _MyArgumentParser


def main():
    """
    Read data from the data file
    and print it to console
    """
    my_argument_parser = _MyArgumentParser()
    my_argument_parser.process_args()

    # if not sys.stdin.isatty():
    #     data = sys.stdin.readlines()
    #     print(data)
    # else:
    #     print("hello")


if __name__ == "__main__":
    main()
