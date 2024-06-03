#!/usr/bin/python3
"""
    Modul that writes an Object to a text file,
    using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file """

    import json

    txt = json.dumps(my_obj)

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(txt)
