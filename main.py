from typing import List, Dict, Any
from Node import Node
import heapq
from heapq import heappop, heappush
import os
import math


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
            # Only assigns code if the node is a leaf node, if it's not, the node is checked
            if node.left is None and node.right is None:
                if len(code) > 0:
                    code_dict[node.char] = code
            else:
                calc_code_for_char(code + '0', node.left)
                calc_code_for_char(code + '1', node.right)
        else:
            return

    calc_code_for_char("", root_node)
    return code_dict


# Compressing the text provided
def compress_text(text: str, file):
    """
    Uses the previously generated optimised character codes to create a file with the compressed text
    :param text: The provided non-compressed text
    :param file: The original file's name
    :return: The file name of the compressed file
    """
    compressed_array = []
    compressed_text = ""
    file_name = ""
    for character in text:
        compressed_text += code_dict.get(character)
        compressed_array.append(int(code_dict.get(character), base=2))
    file_name += file[:-4] + "_compressed"

    # Writing to compressed file in binary
    with open(file_name, "wb") as compressed_file:
        for item in compressed_array:
            compressed_file.write(item.to_bytes(2, byteorder='big'))

    return file_name
    # TODO: Add letter frequencies to generate tree later for decompression


# Decompressing files
def decompress_text(code_dict, compressed_file):
    with open(compressed_file, "rb") as compressed_file:
        byte_array = bytearray(compressed_file.read())

    compressed_text = ""
    for i in byte_array:
        compressed_text += (bin(i))
    list_of_codes = compressed_text.split("0b")
    for i in range(len(list_of_codes)):
        list_of_codes[i] = "0b" + list_of_codes[i]

    decoded_text = ""
    # Converting string values in code_dict to binary values
    for code in code_dict:
        code_dict[code] = bin(int(code_dict.get(code), base=2))
    # Reversing dictionary values so it can be used for decoding
    code_dict = dict(zip(code_dict.values(), code_dict.keys()))
    print(code_dict)
    #print(list_of_codes)
    for code in list_of_codes:
        decoded_text += str(code_dict.get(code))

    print(decoded_text)


# Tidying up testing
def test_program():
    text = ""
    while text == "":
        file = input("Which .txt file would you like to encode eg. file.txt (must be in current program directory)\n")
        try:
            text = get_text_from_file(file)
        except:
            print("File '" + file + "' was not found, the file was empty, or was not a supported filetype (.txt). "
                                    "Please enter a valid filename\n")
    print("Generating tree for " + file + "...")
    root_node = create_huffman_tree(text)
    print("Generating codes using the generated tree...")
    codes = create_codes(root_node)
    print("Compressing text...\n")
    compressed_file = compress_text(codes, text, file)
    file_size = os.path.getsize(file)
    compressed_file_size = os.path.getsize(compressed_file)
    reduction = math.floor(((file_size - compressed_file_size) / file_size) * 100)
    print("File " + file + " has successfully been compressed. The resulting compressed file has been stored as the "
                           "file: " + compressed_file + " \n"
                                                        "The original file's size was " + str(
        file_size) + " bytes, the compressed version's size is " +
          str(compressed_file_size) + " bytes, a " + str(reduction) + "% reduction in size")
    decompress_text(codes, compressed_file)


# Main code to run all of the above
if __name__ == '__main__':
    test_program()
