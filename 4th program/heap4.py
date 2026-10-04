heap = [50, 30, 40, 10, 20]

print("Before deletion:", heap)
deleted = heap[0]

heap[0] = heap[-1]
heap.pop()

i = 0

while True:
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < len(heap) and heap[left] > heap[largest]:
        largest = left

    if right < len(heap) and heap[right] > heap[largest]:
        largest = right

    if largest == i:
        break

    heap[i], heap[largest] = heap[largest], heap[i]
    i = largest

print("Deleted:", deleted)
print("After deletion:", heap)
