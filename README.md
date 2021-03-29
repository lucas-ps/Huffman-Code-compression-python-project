# Huffman Tree Compression Python
 
# Data Structures and Algorithms - Data Compression Coursework
My coursework project for my Data Structures and Algorithms module - Huffman Coding compression algorithm
in Python. Hosted on: [Github](https://github.com/lucas-ps/Huffman-Code-compression-python-project/)

The project takes in a .TXT file and (from my testing) is capable of reducing the file's size by up to 45% using Huffman
Coding

## Requirements
- Python >= 3.7
- Modules used:
  * json
  * typing
  * heapq
  * OS
  * math
  * bitstring

## Usage

To run program, simply run the main.py file. I used the bee movie script for testing, it's been uploaded to the github 
repo so if you would like to test using that, enter 'bee.txt' as your first input in the program
## Main functions

#### get_text_from_file(file: str)
Returns a string of the text data in a provided file
#### calc_letter_frequencies(text: str)
Returns a list with characters in the provided string and their frequencies in descending order
#### create_huffman_tree(text: str)
Creates all necessary nodes to construct a huffman coding tree, returns the root node of the tree
#### create_codes(root_node: Node) 
Assigns optimised huffman codes to each letter using the provided tree
- ####def calc_code_for_char(code: str, node: Node)
  * Recursive function  within create_codes() that checks assigns codes to nodes (characters)
#### def compress_text(text: str, file, code_dict = None)
Uses generated optimised character codes to create a BIN file with the compressed text and a JSOn file with the 
character codes
#### def decompress_text(compressed_file, code_dict=None)
Reads the provided compressed file and it's character codes file, decodes, and writes decoded data to new file
#### def test_program()
Function that calls all other functions to test entire program's functionality
## Node object functions
#### def \_\_init__(self, char, frequency, left=None, right=None)
Constructor for a new node object, creates a node in the tree with defined child nodes
#### def \_\_lt__(self, other):
Defines the behaviour of the less-than operator, overrides the `__lt__()` function to ensure heapq orders nodes
as expected (ascending order of frequency)

## License
[MIT](https://choosealicense.com/licenses/mit/)