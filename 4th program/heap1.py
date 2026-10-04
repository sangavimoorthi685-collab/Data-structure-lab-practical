class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = \
                    self.heap[index], self.heap[parent]
                index = parent
            else:
                break
    def display(self):
        print("Min Heap:", self.heap)

h = MinHeap()
h.insert(50)
h.insert(30)
h.insert(40)
h.insert(10)
h.insert(20)

h.display()
