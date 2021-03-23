from typing import List, Dict

from Node import Node
import queue


# Calculate frequencies of each letter in string provided
def calc_letter_frequencies(text: str) -> list:
    """
    Returns a list with characters in the provided string and their frequencies in descending order
    :param text: The provided string text
    :return: A list with characters and their frequencies (stored as tuples)
    """
    char_frequencies: Dict[str, int] = {}  # Creating dictionary to store characters (str) and their frequencies (int)
    for character in text:
        if character in char_frequencies:
            char_frequencies[character] += 1
        else:
            char_frequencies[character] = 1

    # Sorting the dictionary in descending order of frequencies
    char_frequencies_sorted: List[tuple] = sorted(char_frequencies.items(), key=lambda x: x[1])
    return char_frequencies_sorted


# Creating hoffman tree 
def create_tree(text: str) -> Node:
    char_frequencies = calc_letter_frequencies(text)
    while len(char_frequencies) > 1:  # Until only root node remains
        left_node = char_frequencies[0]
        right_node = char_frequencies[1]  # Getting two nodes with lowest frequency
        node = Node(left_node, right_node)  # Creating the node
        frequencies_to_remove = [char_frequencies[0], char_frequencies[1]]
        char_frequencies = char_frequencies - frequencies_to_remove  # Removing processed characters
        node_frequency = (node, left_node[1] + right_node[1])
        char_frequencies.append(node_frequency)  # Adding new node object back into frequency list
        char_frequencies = sorted(char_frequencies.items(), key=lambda x: x[1])  # Sorting list by ascending frequency
    root_node = char_frequencies[0][0]
    return root_node


# Testing code above with sample text
if __name__ == '__main__':
    text = "text123 this is a test"
    print(calc_letter_frequencies(text))
