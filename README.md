# Huffman coding in Python
My coursework project for my Data Structures and Algorithms module - Huffman Coding compression algorithm
in Python. A demonstration of the program in use can be found [here](https://youtu.be/DxHaksITq3M). Hosted on: [Github](https://github.com/lucas-ps/Huffman-Code-compression-python-project/)

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
- def calc_code_for_char(code: str, node: Node)
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

## Performance analysis

<div class="center">

![E-book compression analysis graph](/files/compression_results_for_e-books.png)

|                    |                       |                         |                          |
|:-------------------|:----------------------|:------------------------|:-------------------------|
| File name          | Original size (bytes) | Compressed size (bytes) | % reduction in file size |
| French E-Book 1    | 346563                | 202010                  | 41.71%                   |
| French E-Book 2    | 1108709               | 600656                  | 45.82%                   |
| English E-Book 1   | 860669                | 476703                  | 44.61%                   |
| English E-Book 2   | 860669                | 476703                  | 44.61%                   |
| Portugese E-Book 1 | 302358                | 168707                  | 44.20%                   |
| Portugese E-Book 2 | 51321                 | 32565                   | 36.55%                   |

![Compression analysis by language](https://github.com/lucas-ps/Huffman-Code-compression-python-project/blob/5b748d4d85ac6b99e12f8a6cd26878f22b71cb03/files/Average%20%25%20file%20size%20reduction%20(E-Books).png)

|                      |                                  |     |     |
|:---------------------|:---------------------------------|:----|:----|
| Compression language | Average % reduction in file size |     |     |
| French E-Books       | 43.77%                           |     |     |
| English E-Books      | 44.61%                           |     |     |
| Portugese E-Books    | 40.37%                           |     |     |

</div>

  
As seen in the data above, Huffman coding is able to fairly consistently
reduce file sizes for all languages tested by 35 - 45%

<div class="center">

![Compression analysis for datasets](/files/compression_results_for_datasets.png)

|                               |                       |                         |                          |
|:------------------------------|:----------------------|:------------------------|:-------------------------|
| Data set name and type        | Original size (bytes) | Compressed size (bytes) | % reduction in file size |
| dblp.xml.00001.1(pseudo-real) | 104857600             | 68781321                | 34.41%                   |
| Escherichia_Coli(real)        | 112689515             | 31648046                | 71.92%                   |
| fib41(artificial)             | 267914296             | 33489307                | 87.50%                   |

</div>

  
As seen in the data above, reduction in file size varies a lot with data
sets as they may have differing levels of repetitiveness

## List of resources used to implement compression algorithm

-   https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/ -
    General intro to Huffman coding

-   https://pypi.org/project/bitstring/ - Documentation used to
    understand writing to binary files

-   https://docs.python.org/3/library/heapq.html - Documentation used to
    understand priority queues in python

-   https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm -
    Understanding how to implement a binary tree in python

  [image]: compression_results_for_e-books.png
  [1]: Averagefilesizereduction(E-Books).png
  [2]: compression_results_for_datasets.png

## License
[MIT](https://choosealicense.com/licenses/mit/)
