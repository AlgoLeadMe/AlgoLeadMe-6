a,b,c,d,e,f = map(int, input().split())

tA = a*d
tB = b*d
tC = c*d
tD = d*a
tE = e*a
tF = f*a

tB -= tE
tC -= tF

y = tC/tB

x = (f-e*y) / d
print(int(x), int(y))