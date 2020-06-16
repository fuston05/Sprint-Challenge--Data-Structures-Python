from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.lastOverwrittenNode = None

    def append(self, item):
        # check cap
        if len(self.storage) < self.capacity:
            # if less than cap, add to end
            self.storage.add_to_tail(item)
        else:
            if len(self.storage) == self.capacity:
                # if cap is full, but nothing new has been added yet
                if self.lastOverwrittenNode == None:
                    self.storage.remove_from_head()
                    self.storage.add_to_head(item)
                    # set lastOverwrittenNode
                    self.lastOverwrittenNode = self.storage.head
                # cap == full, things have been added
                else:
                    # if tail was last one to be overwritten
                    if self.lastOverwrittenNode == self.storage.tail:
                        # set head to be next to get overwritten
                        self.lastOverwrittenNode = self.storage.head
                        self.lastOverwrittenNode.value = item
                    else:
                        # if tail was not last to be overwritten,
                        # overwrite "next"
                        self.lastOverwrittenNode = self.lastOverwrittenNode.next
                        self.lastOverwrittenNode.value = item

    def get(self):
        # return all elements values that are not None
        # returns as a list in given order
        data_list = []
        currentNode = self.storage.head

        while currentNode is not None:
            if currentNode.value is not None:
                data_list.append(currentNode.value)
                currentNode = currentNode.next
        return data_list
