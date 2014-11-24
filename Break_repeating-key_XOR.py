#import binascii
import base64

test1 = 'this is a test'
test2 = 'wokka wokka!!!'

def binary(input_string):
	output_string = ''
	for x in input_string:
		output_string += bin(ord(x))[2:].zfill(8)
	return output_string

def hamming_distance(s1, s2):
    #Return the Hamming distance between equal-length sequences
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1,s2))
	
	
#print(binary(test1))
#print(binary(test2))
#bin(int(binascii.hexlify('hello'), 16))
print(hamming_distance(binary(test1),binary(test2)))

base64textfile = open('6.txt').read() 
textfile = base64.b64decode(base64textfile)
hamdistance = [[0 for x in range(0,70)] for x in range(0,40)] 
linenum = 0
for line in textfile:
	#print(line)
	linenum += 1
	for keysize in range(2,40):
		if (2*keysize < 30):
			ciphertext1 = line[:keysize]
			ciphertext2 = line[keysize:(keysize*2)]
			#print(keysize)
			#print(linenum)
			hamdistance[keysize][linenum] = (hamming_distance(binary(ciphertext1),binary(ciphertext2))/keysize)
			#print('keysize: ', keysize, ' hamming distance: ', hamdistance)
for x in range(0,40):
	averageham = 0
	for y in range(0,linenum):
		averageham += hamdistance[x][y]
	print('keysize: ', x, 'average ham distance:', averageham)
#print(hamdistance)
				
	
		
		