heap = []
def insert(value):
    heap.append(value)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] < heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break
insert(50)
insert(30)
insert(40)
insert(10)
insert(20)
print("Max Heap:", heap)
