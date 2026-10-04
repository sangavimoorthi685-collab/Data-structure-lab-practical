heap = [10, 20, 40, 50, 30]
print("Before deletion:", heap)
deleted = heap[0]
heap[0] = heap[-1]
heap.pop()
i = 0
while True:
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < len(heap) and heap[left] < heap[smallest]:
        smallest = left
    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right
    if smallest == i:
        break
    heap[i], heap[smallest] = heap[smallest], heap[i]
    i = smallest
print("Deleted:", deleted)
print("After deletion:", heap)
