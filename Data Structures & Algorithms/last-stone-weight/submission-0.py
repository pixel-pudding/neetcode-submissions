class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while (len(stones) > 1):

            # Sort in descending order
            # So the two heaviest stones are at index 0 and 1
            stones.sort(reverse=True)

            # Take the two heaviest stones
            x = stones[0]
            y = stones[1]

            # If both stones have the same weight,
            # both are destroyed
            if x == y:
                stones.pop(0)
                stones.pop(0)

            # If x is heavier than y,
            # y is destroyed and x becomes x-y
            else:
                stones.pop(0)       # remove x
                stones.pop(0)       # remove y

                stones.append(x - y) # add the remaining stone

        # If one stone remains, return its weight
        if len(stones) == 1:
            return stones[0]

        # If no stones remain
        return 0