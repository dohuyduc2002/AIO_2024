"""This module define function for AIO2024 Module 1 week 2 exercise."""
from typing import Dict

def word_count(file_path: str)-> Dict[str,int]:
    """_summary_

    Args:
        file_path (str): _description_

    Returns:
        Dict[str,int]: _description_
    """
    count_dict: Dict[str,int] = {}
    with open(file_path,"r",encoding='utf-8') as readfile:
        for line in readfile:
            words = line.lower().strip().split()
            for word in words:
                count_dict[word] = count_dict.get(word,0) + 1
    return count_dict

PATH = '/Users/microwave/AIO_2024/Week_2/P1_data.txt'
print(word_count(PATH))
