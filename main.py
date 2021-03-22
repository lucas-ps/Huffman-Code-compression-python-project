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
    char_frequencies_sorted: List[tuple] = sorted(char_frequencies.items(), key=lambda x: x[1], reverse=True)
    return char_frequencies_sorted


# Creating tree of nodes
def create_tree(text: str):
    char_frequencies = calc_letter_frequencies(text)
    character_queue = queue.PriorityQueue()  # Creating priority queue to work with
    for character in char_frequencies:
        character_queue.put(character)  # Adding tuples for each character with their character and frequency to queue
    while character_queue.qsize() > 1:  # Until there is only one node left (root node?)
        left_node = character_queue.get()
        right_node = character_queue.get()  # Getting values in queue with the smallest frequencies to create a node
        name = left_node[1] + right_node[1]  # Calculating sum of frequencies for the node's name
        name = Node(left_node, right_node)  # Creating the node
    return character_queue.get()  # Returning first node in queue (root node of tree)


# Testing code above with sample text
if __name__ == '__main__':
    text = "text123 this is a test"
    root_node = create_tree(text)
    print(root_node)
