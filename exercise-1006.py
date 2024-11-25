a = float(input())
while (a < 0.0 or a > 10.0) :
    a = float(input())
b = float(input())
while (b < 0.0 or b > 10.0) :
    b = float(input())
c = float(input())
while (c < 0.0 or c > 10.0) :
    c = float(input())
pa = 2.0
pb = 3.0
pc = 5.0
media = (a*pa+b*pb+c*pc)/(pa+pb+pc)
print('MEDIA =', '{:.1f}'.format(media))