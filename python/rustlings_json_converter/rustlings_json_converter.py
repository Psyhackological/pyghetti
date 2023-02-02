"""
This module contains only main function
"""
from collections import defaultdict
import pprint
import json


def main():
    """Main function that converts the "exercises.txt" file to a JSON file.
    The "exercises.txt" file contains information
    about different categories and their corresponding files.
    This function reads the file, converts the information into a dictionary,
    and writes it to a JSON file.
    """
    rustlings_dict = defaultdict(list)

    with open("rustlings.txt", "rt", encoding="utf-8") as rustlings_exercises:
        for line in rustlings_exercises:
            category, *file = line.strip().split(r"/")
            rustlings_dict[category if r"/" in line else "quiz"].append(
                file[0] if file else line.strip()
            )

    pretty_printer = pprint.PrettyPrinter(width=88, compact=True)
    pretty_printer.pprint((dict(rustlings_dict)))

    # writing the dictionary to a JSON file
    with open("rustlings.json", "wt", encoding="utf-8") as rustlings_json:
        json.dump(dict(rustlings_dict), rustlings_json, indent=4)


if __name__ == "__main__":
    main()
