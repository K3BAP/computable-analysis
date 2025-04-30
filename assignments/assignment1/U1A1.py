from decidableset import REAL

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
    print(x.asString(10))

    x = REAL(0, onefifth)
    print(x.asString(10))