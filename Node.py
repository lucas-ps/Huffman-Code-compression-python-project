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

    # Override the `__lt__()` function to make `Node` class work with priority queue
    # such that the highest priority item has the lowest frequency
    # TODO: Check this
    def __lt__(self, other):
        return self.frequency < other.frequency

