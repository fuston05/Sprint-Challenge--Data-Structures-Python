# Each ListNode holds a reference to its previous node
# as well as its next node in the List.

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    # Wrap the given value in a ListNode and insert it
    # after this node. Note that this node could already
    # have a next node it is point to.

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    # Wrap the given value in a ListNode and insert it
    # before this node. Note that this node could already
    # have a previous node it is point to.

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    # Rearranges this ListNode's previous and next pointers
    # accordingly, effectively deleting this ListNode.

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        # heads next
        if self.next:
            self.next.prev = self.prev


# Our doubly-linked list class. It holds references to
# the list's head and tail nodes.


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    # Wraps the given value in a ListNode and inserts it
    # as the new head of the list. Don't forget to handle
    # the old head node's previous pointer accordingly.

    def add_to_head(self, value):
        if self.head:
            newNode = ListNode(value, None, self.head)
            newNode.insert_before(self.head)
            self.head = newNode
            self.length += 1
        else:
            newNode = ListNode(value)
            self.head = newNode
            self.tail = newNode
            self.length += 1

    # Removes the List's current head node, making the
    # current head's next node the new head of the List.
    # Returns the value of the removed Node.

    def remove_from_head(self):
        currentHead = self.head
        curValue = currentHead.value
        self.delete(currentHead)
        return curValue

    # Wraps the given value in a ListNode and inserts it
    # as the new tail of the list. Don't forget to handle
    # the old tail node's next pointer accordingly.

    def add_to_tail(self, value):
        # if there's a tail
        if self.length > 0:
            curTail = self.tail
            curTail.next = ListNode(value, curTail, None)
            self.tail = curTail.next
            self.length += 1
        else:
            newNode = ListNode(value, None, None)
            self.head = newNode
            self.tail = newNode
            self.length += 1

    # Removes the List's current tail node, making the
    # current tail's previous node the new tail of the List.
    # Returns the value of the removed Node.

    def remove_from_tail(self):
        currentTail = self.tail
        curValue = currentTail.value
        self.delete(currentTail)
        return curValue

    # Removes the input node from its current spot in the
    # List and inserts it as the new head node of the List.

    def move_to_front(self, node):
        # is this the tail?
        if node is self.tail:
            oldTail = self.remove_from_tail()
            self.add_to_head(oldTail)

        # if node is the head already
        elif node is self.head:
            return None

        # if node is not the tail or the head
        else:
            oldNodeData = self.delete(node)
            self.add_to_head(oldNodeData)

    # Removes the input node from its current spot in the
    # List and inserts it as the new tail node of the List.

    def move_to_end(self, node):
        oldData = self.delete(node)
        self.add_to_tail(oldData)

    # Removes a node from the list and handles cases where
    # the node was the head or the tail

    def delete(self, node):
        data = node.value
        if node == self.head:
            if node.next != None:
                # set new head
                curHead = node
                self.head = curHead.next
                self.head.prev = None
                self.length -= 1
            else:
                self.head = None
                self.tail = None
                self.length = 0

        elif node == self.tail:
            if node.prev != None:
                curTail = node
                # set new tail
                self.tail = curTail.prev
                self.tail.next = None
                self.length -= 1
            else:
                self.tail = None
                self.head = None
                self.length = 0

        else:
            node.delete()
            self.length -= 1
        return data

# Returns the highest value currently in the list

    def get_max(self):
        if self.head:
            current = self.head
            highestValue = self.head.value
            while current.next != None:
                if current.next.value > highestValue:
                    highestValue = current.next.value
                current = current.next
            return highestValue
