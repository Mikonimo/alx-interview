#!/usr/bin/python3
"""
This module contains a function  about lockboxes
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened
        Arg: boxes - a list of lists
    Return: True if all boxes can be opened, else return False"""
    n = len(boxes)
    opened = set([0])  # Start with box 0 unlocked
    keys = set(boxes[0])  # Collect keys from box 0
    to_visit = list(keys)  # Stack or queue to visit other boxes

    while to_visit:
        key = to_visit.pop()
        if key not in opened and key < n:  # Check if the key is valid
            opened.add(key)  # Open the box
            new_keys = boxes[key]  # Collect new keys from this box
            for k in new_keys:
                if k not in keys:  # Avoid redundant keys
                    keys.add(k)
                    to_visit.append(k)

    # Check if all boxes are opened
    return len(opened) == n
