import heapq

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        def closestBike(w_row,w_col):
            min_distance = 2001
            min_b_id = None

            for b_id, (b_row, b_col) in bikes.items():
                distance = abs(b_row-w_row) + abs(b_col-w_col)

                if distance < min_distance:
                    min_b_id = b_id
                    min_distance = distance
            return min_distance, min_b_id

        bikes = dict(enumerate(bikes))
        seen = set()
        assignment = [None]*len(workers)
        heap = []
        for w_id, (w_row, w_col) in enumerate(workers):
            distance, b_id = closestBike(w_row,w_col)
            heapq.heappush(heap,(distance, w_id, b_id))

        while len(seen) < len(workers):
            _, w_id, b_id = heapq.heappop(heap)

            if b_id in seen:
                w_row,w_col = workers[w_id]
                distance, b_id = closestBike(w_row,w_col)
                heapq.heappush(heap,(distance,w_id,b_id))
            else:
                assignment[w_id] = b_id
                seen.add(b_id)
                del bikes[b_id]
        return assignment
