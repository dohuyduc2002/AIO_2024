"""This module define function for AIO2024 Module 1 week 2 exercise."""
from typing import Dict
#Dictionary in python is a hashmap. Hashmap is a array contain key and value, import for convinience

def count_chars(words : str) -> Dict[str, int]:
    """Count chars in a string

    Args:
        words (str): input string

    Returns:
        Dict[str, int]: dictionary of each char and number of apperance
    """
    char_dict: Dict[str, int] = {} # {char : number of apperance}
    for char in range(len(words)):
        char_dict[words[char]] = 1 + char_dict.get(words[char],0)
    #char_dict[words[char]]: key of char_dict is a character in words
    #char_dict.get(words[char],0): using .get method to retrieve key which is char if exist,else 0
    print(char_dict)
    return char_dict

STRING = 'Happiness'
count_chars(STRING)
