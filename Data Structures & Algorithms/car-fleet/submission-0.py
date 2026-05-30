class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse=True)

        fleets = 1
        time = (target - cars[0][0]) / cars[0][1]

        for i in range(1, len(cars)):
            curr = (target - cars[i][0]) / cars[i][1]
            if curr > time:
                fleets += 1
                time = curr
        
        return fleets
        