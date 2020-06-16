
# Binary search trees are a data structure that enforce an ordering over
# the data they store. That ordering in turn makes it a lot more efficient
# at searching for a particular piece of data in the tree.

# This part of the project comprises two days:
# 1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
#    on the BSTNode class.
# 2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
#    on the BSTNode class.



class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the value to the root's value to determine which direction
        # we're gonna go in
        # if the value < root's value
        if value < self.value:
            # go left
            # how do we go left?
            # we have to check if there is another node on the left side
            if self.left:
                # then self.left is a Node
                # now what?
                self.left.insert(value)
            else:
                # then we can park the value here
                self.left = BSTNode(value)
        # else the value >= root's value
        else:
            # go right
            # how do we go right?
            # we have to check if there is another node on the right side
            if self.right:
                # then self.right is a Node
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        currentNode = self
        # if current node is too big
        if currentNode.value > target:
            # go left
            if currentNode.left:
                # increment the currentNode
                currentNode = currentNode.left
                # return for recursion to work
                return currentNode.contains(target)
        elif currentNode.value < target:
            # go right
            if currentNode.right:
                # increment the currentNode
                currentNode = currentNode.right
                # return for recursion to work
                return currentNode.contains(target)
        elif currentNode.value == target:
            # we have a match
            return True
        # if no match found
        else:
            return False

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # current node
        currentNode = self
        fn(currentNode.value)
        if self.left:
            nextLeft = self.left
            nextLeft.for_each(fn)
        if self.right:
            nextRight = self.right
            nextRight.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node=None):
        # everything will get printed... so..

        # if self has a 'left', self is BIGGER
        if self.left:
            self.left.in_order_print(self)

        print(self.value)

        # if self has a 'right', self is SMALLER
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal FIFO

    def bft_print(self, node=None):
        Que = []
        Que.append(self)

        while len(Que) > 0:
            current = Que.pop(0)
            print(current.value)

            if current.left:
                Que.append(current.left)

            if current.right:
                Que.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal LIFO
    def dft_print(self, node=None):
        stack= []
        stack.append(self)

        while len(stack) > 0:
            current= stack.pop(len(stack)-1)
            print(current.value)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
