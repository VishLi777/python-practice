import deal


@deal.inv(lambda buffer: buffer.max_size > 0)
# Реализация структуры данных циклический буфер.
class CircularBuffer:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.__data = [None] * max_size
        self.head = 0
        self.tail = -1

# Return True if the head of the CircularBuffer is equal to the tail,
# otherwise return False
# Runtime: O(1) Space: O(1)
    def is_empty(self):
        return self.tail == self.head

# Return True if the tail of the CircularBuffer is one before the head,
# otherwise return False
# Runtime: O(1) Space: O(1)
    def is_full(self):
        return self.tail == (self.head - 1) % self.max_size

# Insert an item at the back of the CircularBuffer
# Runtime: O(1) Space: O(1)
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("CircularBuffer is full, unable to enqueue item")
        self.tail = (self.tail + 1) % self.max_size
        self.__data[self.tail] = item

# Return the item at the front of the CircularBuffer
# Runtime: O(1) Space: O(1)
    def front(self):
        return self.__data[self.head]

# Return the item at the front of the Circular Buffer and remove it
# Runtime: O(1) Space: O(1)
    def dequeue(self):

        if self.is_empty():
            raise IndexError("CircularBuffer is empty, unable to dequeue")
        item = self.__data[self.head]
        self.__data[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item

    def __getitem__(self, item):
        return self.__data[item]


# to get exception contract
# cb = CircularBuffer(-1)


# import deal
#
#
# Реализация структуры данных циклический буфер.
# @deal.inv(lambda buffer: buffer.max_size > 0)
# class CircularBuffer:
#     def __init__(self, max_size=10):
#         self.max_size = max_size
#         self.__data = [None] * max_size
#         self.head = 0
#         self.tail = -1

#pytest coverage/circ_buffer.py