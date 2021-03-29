import json
from typing import Dict
from Node import Node
import heapq
from heapq import heappop, heappush
import os
import math
from bitstring import BitArray


def get_text_from_file(file: str) -> str:
    """
    :return: String of text data in provided file
    """
    print("\nLoading text as string from file: " + file + "...")
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
    print("Calculating letter frequencies in text provided...")
    char_frequencies: Dict[str, int] = {}  # Creating dictionary to store characters (str) and their frequencies (int)
    for character in text:
        if character in char_frequencies:
            char_frequencies[character] += 1
        else:
            char_frequencies[character] = 1

    # Sorting the dictionary in ascending order of frequencies
    char_frequencies_sorted = sorted(char_frequencies.items(), key=lambda x: x[1])
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
    print("Generating character frequency priority queue for tree generation...")
    for character in char_frequencies:
        char = character[0]
        frequency = character[1]
        queue.append(Node(char, frequency))
    heapq.heapify(queue)  # Sorting queue in descending order of frequencies

    print("Generating huffman tree...")
    while len(queue) > 1:  # Until only root node remains
        testing_output = []
        for item in queue:
            testing_output.append((item.char, "", str(item.frequency)))
        # print(testing_output) # for visualising iterations
        # Choosing 2 letters with lowest frequencies for child nodes, removing them from queue
        left_node = heappop(queue)
        right_node = heappop(queue)
        combined_frequency_of_children = left_node.frequency + right_node.frequency
        heappush(queue, Node(None, combined_frequency_of_children, left_node, right_node))
        heapq.heapify(queue)

    return queue[0]  # Returning root node of tree


# Creating codes for each letter
def create_codes(root_node: Node) -> dict:
    """
    Assigns optimised huffman codes to each letter using the provided tree
    :param root_node: The root node of the tree
    :return: a dictionary of characters and their codes
    """
    code_dict = {}
    print("Creating code dictionary from tree provided...")
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
def compress_text(text: str, file, code_dict = None):
    """
    Uses generated optimised character codes to create a BIN file with the compressed text and a JSOn file with the
    character codes
    :param text: The provided non-compressed text
    :param file: The original file's name
    :return: The file name of the compressed file
    """

    file_name = file + "_compressed.bin"
    if code_dict is None:
        code_dict = create_codes(create_huffman_tree(text))

    # Adding each character's code to a bitarray and writing it all to a file
    binary_output = BitArray()
    print("Encoding text using code dictionary...")
    for character in text:
        binary_output.append('0b' + code_dict[character])
    print("Writing encoded text to: " + file_name + "...")
    with open(file_name, "wb+") as bin_file:
        bin_file.write(binary_output.tobytes())
    print("Writing huffman character codes to: " + file_name + "_codes.json...")
    with open(file_name + "_codes.json", 'w') as code_file:
        code_file.write(json.dumps(code_dict))
    return file_name


# Decompressing files
def decompress_text(compressed_file, code_dict=None):
    """
    Reads the provided compressed file and it's character codes file, decodes, and writes decoded data to new file
    :param compressed_file: The filename of the previously compressed file to be decompressed
    :param code_dict: Optional parameter, the dictionary with all character codes
    :return: The filename of the decompressed file output
    """
    print("Reading compressed.bin file: " + compressed_file)
    with open(compressed_file, "rb") as compressed_file:
        raw_binary = compressed_file.read()

    binary_string = ""
    decoded_string = ""

    if code_dict is None:
        if code_dict is None:
            json_file = (compressed_file.name + "_codes.json")
            print("Loading JSON codes file: " + json_file + "...")
            with open(json_file, 'r') as file:
                data = file.read()
                code_dict = json.loads(data)

    print("Decoding binary using codes extracted...")
    # Extracting one bit at a time until a code match for the character has been found
    for code in BitArray(raw_binary).bin:
        binary_string += str(code)
        for character in code_dict:
            if code_dict[character] == binary_string:
                decoded_string += character
                binary_string = ""

    decompressed_filename = str(compressed_file.name) + "_decompressed.txt"
    print("Writing decoded text to .txt file: " + decompressed_filename + "...")
    with open(decompressed_filename, "w") as decompressed_file:
        decompressed_file.write(decoded_string)

    return decompressed_filename


# Tidying up testing
def test_program():
    text = ""
    while text == "":
        file = input('\033[1m' + "Which .txt file would you like to encode eg. file.txt (must be in current program "
                     "directory)\n" + '\033[0m')
        try:
            text = get_text_from_file(file)
        except:
            print('\033[1m' + "File '" + file + "' was not found, the file was empty, or was not a supported filetype "
                  "(.txt). Please enter a valid filename\n" + '\033[0m')
    compressed_file = compress_text(text, file)
    file_size = os.path.getsize(file)
    compressed_file_size = os.path.getsize(compressed_file)
    json_file_size = os.path.getsize(compressed_file + "_codes.json")
    total_size_compressed = compressed_file_size + json_file_size
    reduction = math.floor(((file_size - compressed_file_size - json_file_size) / file_size) * 100)
    print('\033[1m' + "\nFile " + file + " has successfully been compressed. The resulting compressed file has been "
         "stored as the file: " + compressed_file + " \nThe original file's size was " + str(file_size) + " bytes, the "
         "compressed version's size (including JSON file for character codes) is " + str(total_size_compressed) +
         " bytes, a " + str(reduction) + "% reduction in size\n" + '\033[0m')
    decompressed_file = decompress_text(compressed_file)
    decompressed_file_size = os.path.getsize(decompressed_file)
    print('\033[1m' + "\n" + compressed_file + " successfully decompressed. The original file's size was " +
          str(file_size) + " bytes, the decompressed file's size is " + str(decompressed_file_size) + " bytes, if these"
          " numbers are equal, then no data was lost in compression / decompression.\nThe decompressed file has been "
          "stored as: " + decompressed_file + '\033[0m')


# Main code to run all of the above
if __name__ == '__main__':
    test_program()
