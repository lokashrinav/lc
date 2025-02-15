class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            image[i] = image[i][::-1]
        
        for i in range(len(image)):
            for p in range(len(image[0])):
                image[i][p] ^= 1
        
        return image
