class REAL:
    def __init__(self, x: int, set_a: callable):
        self.x = x
        self.set_a = set_a

    def toString(self, n):
        ret = "."
        y = self.x

        # Convert whole number
        if y == 0:
            ret = "0" + ret
        while y > 0:
            ret = str(y % 2) + ret
            y //= 2

        # Convert set a
        for i in range(n):
            if self.set_a(i):
                ret = ret + "1"
            else:
                ret = ret + "0"

        return ret

# Menge A für 1/3. Bestimme je, ob n in Menge A enthalten ist.
def onethird(n):
    if n % 2 == 1:
        return True
    else:
        return False

# Menge A für 1/5
def onefifth(n):
    if n % 4 in [2, 3]:
        return True
    else:
        return False

if (__name__ == "__main__"):
    x = REAL(0, onethird)
    print(x.toString(10))

    x = REAL(0, onefifth)
    print(x.toString(10))