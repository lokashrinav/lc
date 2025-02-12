# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        curr = street

        for i in range(k):
            curr.openDoor()
            curr.moveRight()
        
        count = 0
        for i in range(k):
            if street.isDoorOpen() is False:
                break
            count += 1
            street.closeDoor()
            street.moveRight()
        
        return count
        