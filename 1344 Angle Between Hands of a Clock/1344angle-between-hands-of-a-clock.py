class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteAngle = minutes * 6
        hourAngle = 30 * (hour % 12) + (0.5 * minutes)
        total = abs(hourAngle - minuteAngle)
        return min(total, 360 - total)