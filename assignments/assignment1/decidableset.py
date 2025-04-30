class REAL:
    def __init__(self, x: int, set_a: callable):
        self.x = x
        self.set_a = set_a

    def asString(self, n):
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

