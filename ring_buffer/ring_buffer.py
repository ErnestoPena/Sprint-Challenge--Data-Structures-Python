from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.current.value = item
            self.current = self.storage.head if self.current == self.storage.tail else self.current.next    


    def recursive_method(self, list_item, the_array):
        if list_item is None:
            return the_array
        else:
            return self.recursive_method(list_item.next, [*the_array, list_item.value])    


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        list_buffer_contents = self.recursive_method(self.storage.head, list_buffer_contents)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


test = RingBuffer(5)
test.append(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)

print(test.get())
