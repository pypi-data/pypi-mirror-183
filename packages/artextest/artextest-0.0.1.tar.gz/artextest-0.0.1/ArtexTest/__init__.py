def getGCD(m, n):
    while True:
        m = m % n # 1. [Remainder m/n.]
        if m == 0: # 2. [Is it zero?] 
            return n

        n = n % m # 3. [Remainder n/m.]
        if n == 0: # 4. [Is it zero?] 
            return m