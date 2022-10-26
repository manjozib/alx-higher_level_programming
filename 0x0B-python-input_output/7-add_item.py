#!/usr/bin/python3
"""
Module 7-add_item
"""
import json
import os
import sys


def load_from_json_file():
    """
    a function that creates an Object from a “JSON file”

    """
    with open("add_item.json", mode='r', encoding='UTF8') as my_file:
        data = json.load(my_file)
        return data


def save_to_json_file(my_obj):
    """
    a function that writes an Object to a text file, using a JSON
    representation

    Args:
        my_obj (object): object

    Return:
    """
    json_object = json.dumps(my_obj)
    with open("add_item.json", mode='w', encoding='UTF8') as my_file:
        my_file.write(json_object)


def do_everything(data):
    """
    a function that creates an empty json if it doesn't exist
    else it will append to the available data
    Args:
        data (list): ity is taken from command line arguments
    Returns:
    """
    is_exists = os.path.exists('add_item.json')
    if is_exists:
        fetch_data = load_from_json_file()
        save_to_json_file(fetch_data + data)
    else:
        save_to_json_file(data)


n = len(sys.argv)
add_item_list = []
for i in range(1, n):
    add_item_list.append(sys.argv[i])


do_everything(add_item_list)
