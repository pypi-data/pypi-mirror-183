import argparse
import fileinput
import json
import numbers
import sys

from jsonpath_tp import get
from treepath import MatchNotFoundError


class _MyArgumentParser:
    __slots__ = (
        "parser",
    )

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.__description, epilog=self.__epilog)

        output_group = self.parser.add_argument_group(title="output",
                                                      description="Specify how the output shall be formated")
        group = output_group.add_mutually_exclusive_group()
        group.add_argument("--list", dest="output", action='store_const', const=self.list_, default=self.lines)
        group.add_argument("--lines", dest="output", action='store_const', const=self.lines)
        group.add_argument("--values", dest="output", action='store_const', const=self.value)

        output_group.add_argument("--indent", type=int, default=None)
        output_group.add_argument("--sort_keys", action='store_true')

        self.parser.add_argument(
            'jsonpath',
            help="The jsonpath query"
        )

        def read_stdin(*args, **kwargs):
            pass

        self.parser.add_argument(
            'json_files',
            nargs='*',
            help=" '-' for stdin or one or more file paths to json documents",
            type=argparse.FileType('r')
        )

    @property
    def __description(self):
        return "Python jsonpath cli utility."

    @property
    def __epilog(self):
        return """
        The jsonpath_cli is a jsonpath implementation built on top of treepath technology.  For details see:
        https://pypi.org/project/jsonpath-tp/
        """

    def process_args(self):
        parsed_args = self.parser.parse_args()
        parsed_args.output(parsed_args, self.process_get)

    def list_(self, parsed_args, process_func):
        my_list = list()
        for result in process_func(parsed_args):
            my_list.append(result)

        print(self.json_dumps(my_list, parsed_args), file=sys.stdout)

    def lines(self, parsed_args, process_func):
        for result in process_func(parsed_args):
            print(self.json_dumps(result, parsed_args), file=sys.stdout)

    def value(self, parsed_args, process_func):
        for result in process_func(parsed_args):
            if isinstance(result, str):
                print(result, file=sys.stdout)
            elif isinstance(result, bool):
                print(self.json_dumps(result, parsed_args), file=sys.stdout)
            elif isinstance(result, numbers.Number):
                print(result, file=sys.stdout)
            else:
                print(self.json_dumps(result, parsed_args), file=sys.stdout)

    def process_get(self, parsed_args):

        last_outer_nf = None

        for json_file in parsed_args.json_files:
            json_data = json.load(json_file)
            try:
                result = get(parsed_args.jsonpath, json_data)
                yield result
                last_outer_nf = None
                break
            except MatchNotFoundError as nf:
                last_outer_nf = nf

        if last_outer_nf is not None:
            raise last_outer_nf

    def json_dumps(self, obj, parsed_args) -> str:
        indent = parsed_args.indent
        sort_keys = parsed_args.sort_keys
        return json.dumps(obj, indent=indent, sort_keys=sort_keys)
