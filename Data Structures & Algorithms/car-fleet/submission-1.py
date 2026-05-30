class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse=True)

        stack = [cars[0]]
        time = (target - cars[0][0]) / cars[0][1]

        for pos, sp in cars:
            curr = (target - pos) / sp
            if curr > time:
                stack.append((pos, sp))
                time = curr
        
        return len(stack)
        