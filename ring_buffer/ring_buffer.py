from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity= 1000
        self.storage= DoublyLinkedList()

    def append(self, item):
        # check cap
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            # remove old head
            self.storage.remove_from_head()
            # add new node as the new head
            self.storage.add_to_head(item)

    def get(self):
        pass