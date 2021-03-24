# Tree node class for storage of characters
class Node:
    def __init__(self, char, left=None, right=None, frequency=None):
        """
         Constructor for a new node, creates a node in the tree with defined child nodes
        :param left:
        :param right:
        """
        self.char = char
        self.left = left
        self.right = right
        if frequency is None:
            frequency = self.calcFrequency()
        self.frequency = frequency

    # Override the `__lt__()` function to make `Node` class work with priority queue
    # such that the highest priority item has the lowest frequency
    # TODO: Check this
    def __lt__(self, other):
        return self.frequency < other.frequency

    def calcFrequency(self) -> int:
        """
        Calculates the frequency of a non leaf node (when frequency is not provided)
        """
        try:
            if self.left is not None:
                if self.right is not None:
                    frequency = self.left[0].getFrequency() + self.right[0].getFrequency()
                else:
                    frequency = self.left[0].getFrequency()
            elif self.right is not None:
                frequency = self.right[0].getFrequency()
            else:
                raise Exception("Node provided is a leaf node, no frequency was provided")
        except:
            frequency = 0
        return frequency

    def children(self):
        """
        Returns the node's child nodes
        :return: Node objects of the node's children
        """
        return self.left, self.right

    def nodes(self):
        """
        #TODO: not 100% sure
        :return:
        """
        return self.left, self.right

    def __str__(self):
        return str(self.left), "--", str(self.right)
