class Solution:
    def reachNumber(self, target):
        target = abs(target)  # Step 1: Convert to positive

        # Step 2: Compute initial k using the quadratic formula
        k = math.ceil((-1 + math.sqrt(1 + 8 * target)) / 2)
        
        # Step 3: Compute the cumulative sum S
        S = k * (k + 1) // 2
        
        # Step 4: Compute the difference D
        difference = S - target
        
        # Step 5: Check if D is even
        if difference % 2 == 0:
            return k
        else:
            return k + 1
            # Determine if the next k+1 is odd or even
            if (k + 1) % 2 == 1:
                # If k+1 is odd, one more increment suffices
                return k + 1
            else:
                # If k+1 is even, two more increments are needed
                return k + 2
