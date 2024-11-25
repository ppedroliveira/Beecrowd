a = float(input())
while (a < 0.0 or a > 10.0) :
    a = float(input())
b = float(input())
while (b < 0.0 or b > 10.0):
    b = float(input())
pa = 3.5
pb = 7.5
media = (a*pa+b*pb)/(pa+pb)
print('MEDIA =', '{:.5f}'.format(media))