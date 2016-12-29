class Heap:

    def __init__(self, nums):
        self.heap = [0] * (len(nums) + 1)
        self.size = 0
        self.__init_heap(nums)


    def __init_heap(self, nums):
        for i in range(len(nums)):
            self.enqueue(nums[i])


    def enqueue(self, val):
        i = self.size + 1
        self.heap[i] = val
        while i > 1 and self.heap[i // 2] < self.heap[i]:
            self.heap[i], i = self.heap[i // 2], i // 2
        self.heap[i] = val
        self.size += 1


    def dequeue(self):
        root, i = self.heap[1], 1
        while i * 2 < self.size:
            child = i * 2
            if self.heap[child + 1] < self.heap[child]:
                child += 1
            if child < self.heap[self.size]:
                self.heap[i], i = self.heap[child], child
            else:
                break
        self.heap[i] = self.heap[self.size]
        self.size -= 1
        return root


    def sort(self):
        container = self.heap[1:self.size + 1]
        heap = Heap(container)
        elems = [0] * heap.size
        for i in range(len(elems)):
            elems[i] = heap.dequeue()
        return elems
