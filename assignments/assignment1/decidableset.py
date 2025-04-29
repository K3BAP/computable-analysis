class REAL:
    def __init__(self, x: int, set_a: list):
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
            if i in self.set_a:
                ret = ret + "1"
            else:
                ret = ret + "0"

        return ret

if (__name__ == "__main__"):
    x = REAL(2, [0, 1, 2])

    print(x.toString(3))