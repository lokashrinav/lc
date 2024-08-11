class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        pairs = sorted(pairs, reverse=True)

        fleets = 0
        dist_time = 0
        for pos, spe in pairs:
            destination_time = (target - pos) / spe
            if destination_time > dist_time:
                fleets += 1
                dist_time = destination_time

        return fleets
            





                




        