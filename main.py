from typing import List, Dict, Any
from Node import Node
import queue
import heapq
from heapq import heappop, heappush


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
    for character in char_frequencies:
        char = character[0]
        frequency = character[1]
        queue.append(Node(char, frequency))
    heapq.heapify(queue)

    while len(queue) > 1:  # Until only root node remains
        # Choosing 2 letters with lowest frequencies for child nodes, removing them from queue
        left_node = heappop(queue)
        right_node = heappop(queue)
        combined_frequency_of_children = left_node.frequency + right_node.frequency
        heappush(queue, Node(None, combined_frequency_of_children, left_node, right_node))

    return queue[0]  # Returning root node of tree


# Creating codes for each letter
def create_codes(root_node: Node) -> dict:
    """
    Assigns optimised huffman codes to each letter using the provided tree
    :param root_node: The root node of the tree
    :return: a dictionary of characters and their codes
    """
    code_dict = {}

    def calc_code_for_char(code: str, node: Node) -> str:
        """
        Recursive function that checks assigns codes to nodes (characters)
        :param code: The current code for the transversal path
        :param node: The node being operated on
        """
        # Checking if node exists
        if node is not None:
            # Checking if node provided is a leaf node (can have char assigned to it)
            print(node.frequency)
            if node.left is None and node.right is None:
                if len(code) > 0:
                    code_dict[node.char] = code
                else:
                    code_dict[node.char] = '1'
            calc_code_for_char(code + '0', node.left)
            calc_code_for_char(code + '1', node.right)
        else:
            return

    calc_code_for_char("", root_node)
    return code_dict


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
    codes = create_codes(root_node)
    print(codes)
