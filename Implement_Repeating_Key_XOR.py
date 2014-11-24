from itertools import cycle
line1 = ['Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal']
key = 'ICE'
for line in line1:
    cryptotext = ''
    for b1, b2 in zip(line, cycle(key)):
        cryptotext += chr((ord(b1) ^ ord(b2)))
#        if cryptotext[-1] == '\n':
#            print 'newline'
    print cryptotext.encode('hex')