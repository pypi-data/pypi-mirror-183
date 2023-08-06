import argparse
import json
import sys

from jsonpath_tp import get


class _MyArgumentParser:
    __slots__ = (
        "parser",
    )

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.__description, epilog=self.__epilog)
        self.parser.add_argument(
            'jsonpath',
            help="The jsonpath query"
        )
        self.parser.add_argument(
            'json_files',
            nargs='+',
            help="stdin or one or more file paths to json documents",
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
        args = self.parser.parse_args()

        for json_file in args.json_files:
            json_data = json.load(json_file)
            result = get(args.jsonpath, json_data)
            sys.stdout.write(str(json.dumps(result)))
