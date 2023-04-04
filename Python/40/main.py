fraction = ''
for i in range(1, 1000000+1):
    fraction += str(i)

d1 = int(fraction[0])
d10 = int(fraction[9])
d100 = int(fraction[99])
d1000 = int(fraction[999])
d10000 = int(fraction[9999])
d100000 = int(fraction[99999])
d1000000 = int(fraction[999999])

print(d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000)
