import heapq

class KthLargest:

    def __init__(self, k, nums):
        # We need to find the kth largest element
        self.k = k

        # Python's heapq is a MIN HEAP
        # We will maintain only the largest k elements in this heap
        self.heap = []

        # Add all the initial numbers to the heap
        for num in nums:
            heapq.heappush(self.heap, num)

            # If we have more than k elements,
            # remove the smallest element
            #
            # This ensures that only the largest k elements remain
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val):

        # Add the new value to our heap
        heapq.heappush(self.heap, val)

        # If there are now more than k elements,
        # remove the smallest one
        #
        # Why?
        # We only want to keep the largest k elements
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Since this is a MIN HEAP,
        # the smallest element is always at index 0
        #
        # Among the largest k elements,
        # the smallest one is the kth largest overall
        return self.heap[0]