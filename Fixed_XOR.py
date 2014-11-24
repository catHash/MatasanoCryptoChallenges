a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'
binary_a = a.decode('hex')
binary_b = b.decode('hex')
#print a
#print b
#print binary_a
#print binary_b
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))
xored = xor_strings(binary_a, binary_b).encode('hex')
print xored