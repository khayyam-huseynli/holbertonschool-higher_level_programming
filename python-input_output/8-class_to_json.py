#!/usr/bin/python3
"""
    Modul that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object
"""


def class_to_json(obj):
    """
        Function that returns the JSON representation
        of an instance of a Class
    """

    import json
    return json.dumps(obj.to_json())
