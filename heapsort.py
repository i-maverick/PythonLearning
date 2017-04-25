import heapq


def heap_sort(_lst):
    heapq.heapify(_lst)
    return [heapq.heappop(_lst) for _ in range(len(_lst))]

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print heap_sort(lst)


class PriorityQueue():
    def __init__(self):
        self.pq = []

    def insert(self, obj):
        heapq.heappush(self.pq, obj)

    def pop_min(self):
        return heapq.heappop(self.pq)

    def __len__(self):
        return len(self.pq)


queue = PriorityQueue()
queue.insert((2, 'e'))
queue.insert((4, 'p'))
queue.insert((3, 'a'))
queue.insert((1, 'h'))

print ''.join([queue.pop_min()[-1] for _ in range(len(queue))])
