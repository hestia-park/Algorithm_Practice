class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(pos, (target - pos) / spd) for pos, spd in zip(position, speed)], reverse=True)
        print(cars)
        fleets = 0
        current_time = 0
        
        for pos, time in cars:
            if time > current_time:
                fleets += 1
                current_time = time
        
        return fleets
