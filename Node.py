# Tree node class for storage of characters
class Node:
    def __init__(self, char, frequency, left=None, right=None):
        """
         Constructor for a new node, creates a node in the tree with defined child nodes
        :param left:
        :param right:
        """
        self.char = char
        self.left = left
        self.right = right
        self.frequency = frequency


    def __lt__(self, other):
        """
         Defines the behaviour of the less-than operator, overrides the `__lt__()` function to ensure heapq orders nodes
         as expected (ascending order of frequency)
        :param other: The other node being compared
        :return:
        """
        return self.frequency < other.frequency
