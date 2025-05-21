class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = [0, 0]

        res[0] = celsius + 273.15
        res[1] = celsius * 1.8 + 32

        return res