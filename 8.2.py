import cmath
q = -2.235 * 10**-2
w = 2.23
e = 15.221
a = (cmath.exp(abs(q-w))) * ((abs(q-w))**(q+w))
b = cmath.atan(q) + cmath.atan(e)
c = (q**6 + cmath.log10(w)**2)**(1/3)
s = a/b + c
print(s)