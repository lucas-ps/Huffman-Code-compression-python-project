from typing import List, Dict, Any
from Node import Node
import queue
import heapq


def get_text_from_file(file: str) -> str:
    """
    :return: String of text data in provided file
    """
    file_data = open(file, "r").readlines()
    file_data_str = ''.join(map(str, file_data))
    return file_data_str


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

    # Sorting the dictionary in ascending order of frequencies
    char_frequencies_sorted: List[tuple] = sorted(char_frequencies.items(), key=lambda x: x[1])
    return char_frequencies_sorted


# Creating hoffman tree
def create_huffman_tree(text: str) -> Node:
    """
    Creates all necessary nodes to construct a huffman coding tree, returns the root node of the tree
    :param text: The provided string text
    :return: The root node of the tree
    """
    char_frequencies = calc_letter_frequencies(text)
    # Creating queue of letters and their frequencies
    queue = []
    for character, frequency in char_frequencies.items():
        queue.append(Node(character, frequency))
    heapq.heapify(queue)

    while len(queue) > 1:  # Until only root node remains
        # Choosing 2 letters with lowest frequencies for child nodes, removing them from queue
        left_node = heappop(queue)
        right_node = heappop(queue)
        combined_frequency_of_children = left_node.frequency + right_node.frequency
        heappush(queue, Node(None, left_node, right_node, combined_frequency_of_children))

    return queue[0]  # Returning root node of tree


# Main code to run all of the above
if __name__ == '__main__':
    text = ""
    while text == "":
        file = input("Which file would you like to encode eg. file.txt (must be in current program directory)")
        try:
            text = get_text_from_file(file)
        except:
            print("File '" + file + "' was not found, or the file was empty. Please enter a valid filename")
    root_node = create_huffman_tree(text)
