from decidableset import REAL
from gmpy2 import mpq # rationale Zahlen

a = 41
b = 5
x = REAL( mpq(a,b) )
print ("x:", x.asString(10) )

y = REAL( mpq(1,7) )
print ("y:", y.asString(20) )

z = REAL( mpq(1,11) )
print ("z:", z.asString(30) )