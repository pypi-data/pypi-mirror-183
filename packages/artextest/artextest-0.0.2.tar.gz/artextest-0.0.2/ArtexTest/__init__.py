def getGCD(m, n):
    """
    Given two positive integers m and n, find and return their greatest common divisor, 
    that is, the largest positive integer that evenly divides both m and n.
    """
    while True:
        m = m % n # 1. [Remainder m/n.]
        if m == 0: # 2. [Is it zero?] 
            return n

        n = n % m # 3. [Remainder n/m.]
        if n == 0: # 4. [Is it zero?] 
            return m