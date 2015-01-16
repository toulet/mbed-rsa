from gmpy import invert


b = pow(2, 32)
#b = 10
n = 32
#n = 5


def big_build(l):
	n = 0
	for i in range(0, len(l) - 1):
		n = n + l[i] * pow(2, 32 * i)
	return n


#def extract(n, i):
#	return (n >> (32 * i)) & 0xFFFFFFFF

def extract(n, i):
	return (n / pow(b, i)) % b

#m = big_build([0x990742cd, 0xcc1664eb, 0x996d9ee2, 0xd25a8923, 0xed9b5ce6, 0x1215cda8, 0x8ab1355f, 0x96606fb8, 0x12f9d236, 0x91b1663a, 0xd28ec1c2, 0x3bd68a80, 0xb11f47d2, 0x485b8f94, 0x71d9430a, 0xd8dc6670, 0x019f874b, 0xce3b9052, 0x1d7b3d36, 0x410d52cc, 0x2bd82a0c, 0x140acae7, 0xe9d6d2f5, 0xe898ad4c, 0x90a8f77c, 0x9face9fb, 0x4e3c87af, 0x3d44b55c, 0xed53525f, 0x7e8c95bc, 0x4e8066a1, 0x02813b5d, 0x00000000])
m = big_build([0x990742cd, 0xcc1664eb, 0x996d9ee2, 0xd25a8923, 0xed9b5ce6, 0x1215cda8, 0x8ab1355f, 0x96606fb8, 0x12f9d236, 0x91b1663a, 0xd28ec1c2, 0x3bd68a80, 0xb11f47d2, 0x485b8f94, 0x71d9430a, 0xd8dc6670, 0x019f874b, 0xce3b9052, 0x1d7b3d36, 0x410d52cc, 0x2bd82a0c, 0x140acae7, 0xe9d6d2f5, 0xe898ad4c, 0x90a8f77c, 0x9face9fb, 0x4e3c87af, 0x3d44b55c, 0xed53525f, 0x7e8c95bc, 0x4e8066a1, 0x00000000, 0x00000000])
#m =  72639

#mp = 0x62e185fb
mp = (-invert(m, pow(2,32)) % pow(2, 32))
#mp = 1

r = pow(b, n)
rp = invert(r, m)

#x = big_build([0xecc0ae5d, 0x4a67cec4, 0x5c9afeb2, 0x10a5ff05, 0xb0117eac, 0x846a35ac, 0xbd1a94cc, 0x393dc9a2, 0x1d5cc37f, 0x91511fb9, 0xae287ed8, 0xeb8b8f0e, 0x69031e30, 0x0921a035, 0x22f11a51, 0x9156466b, 0x088f3373, 0x9a3192ee, 0xf021d23d, 0x965165e6, 0xb12a9988, 0x36220967, 0x27b78557, 0xd1a2a1dc, 0x5cb18ced, 0xdbdc3d1c, 0x6bc4dc50, 0x9f2c1354, 0x83413afb, 0xfe44e120, 0xfe3a1aee, 0x7c0f5a7c, 0x00000000])
x = big_build([0xecc0ae5d, 0x4a67cec4, 0x5c9afeb2, 0x10a5ff05, 0xb0117eac, 0x846a35ac, 0xbd1a94cc, 0x393dc9a2, 0x1d5cc37f, 0x91511fb9, 0xae287ed8, 0xeb8b8f0e, 0x69031e30, 0x0921a035, 0x22f11a51, 0x9156466b, 0x088f3373, 0x9a3192ee, 0xf021d23d, 0x965165e6, 0xb12a9988, 0x36220967, 0x27b78557, 0xd1a2a1dc, 0x5cb18ced, 0xdbdc3d1c, 0x6bc4dc50, 0x9f2c1354, 0x83413afb, 0xfe44e120, 0xfe3a1aee, 0x00000000, 0x00000000])
#x = 5792
y = x
#y = 1229

excepted = big_build([0x5fcd745c, 0x0e59b650, 0xbb9fd999, 0x61626903, 0xec4f9528, 0x7615843f, 0xe44eb4bd, 0x77e3dbd8, 0x22536b19, 0x1a6a6176, 0xb66a52c9, 0x5a88e85e, 0x7759235d, 0x957564af, 0xc8c95719, 0x891d88c4, 0xb9b4d3c9, 0xecba6fdb, 0x06a57f5d, 0x0f0b964c, 0x5618da9d, 0x65d8f1c3, 0xac398925, 0xa0c32807, 0xe0fd4c9c, 0x8c0e155d, 0x60622a44, 0xf92c6fbd, 0x05cc2aaa, 0x1d0e32f7, 0x62119e59, 0x02512a00, 0x00000000])


a = 0
u = 0

for i in range(0, n):
	#print "xi : " + str(extract(x, i))
	u = ((extract(a, 0) + extract(x, i) * extract(y, 0)) * mp) % b
	#print "xi*y0 : " + str(extract(x, i) * extract(y, 0))
	tmp1 = extract(x, i) * y
	print hex(tmp1 % pow(b, 32))
	#print "ui : " + str(u)
	#print "xi*y : " + str(tmp1)
	tmp2 = u * m
	print hex(tmp2 % pow(b, 32))
	#print "ui*m : " + str(tmp2)
	a = (a + extract(x, i) * y + u * m) % pow(b, 32) / b
	#a = (a + extract(x, i) * y + u * m) / b
	print hex(a % pow(b, 32))
	#print "a : " + str(a)
	print "\n"

if a > m:
	a = a - m

#for i in range(0, 1000000):
#	if ((x*y*i) % m) == a:
#		print "ICIIIII => " + str(i)
#print rp

out = (x * y * rp) % m

print "HOP"
#print hex(r)
print hex(a)
#print a
#print hex(a * r)
print hex(out)
#print out
#print hex(excepted - a)
#print hex(rp)
