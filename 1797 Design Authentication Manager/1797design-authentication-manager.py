from collections import deque

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}  # tokenId -> expirationTime
        self.queue = deque()  # (tokenId, expirationTime)
    
    def generate(self, tokenId: str, currentTime: int) -> None:
        expirationTime = currentTime + self.timeToLive
        self.tokens[tokenId] = expirationTime
        self.queue.append((tokenId, expirationTime))
    
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            expirationTime = currentTime + self.timeToLive
            self.tokens[tokenId] = expirationTime
            self.queue.append((tokenId, expirationTime))
    
    def countUnexpiredTokens(self, currentTime: int) -> int:
        # Remove expired tokens from the front of the queue
        while self.queue and self.queue[0][1] <= currentTime:
            tokenId, expirationTime = self.queue.popleft()
            if self.tokens.get(tokenId) == expirationTime:
                del self.tokens[tokenId]
        
        return len(self.tokens)
