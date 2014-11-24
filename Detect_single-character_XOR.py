with open('Set_1_Challenge_4.txt', 'r') as openfileobject:
    for line in openfileobject:
        #print 'line: ', line
        line = line.strip()
        bytes = line.decode('hex')
        #print 'bytes: ', bytes
        for byte in range(0,255):
            plaintext = ''
            for x in bytes:
                nextchar = byte ^ ord(x)
                plaintext += chr(nextchar)
            if 'ing' in plaintext:
                print 'byte:',byte, ' plaintext: ',plaintext

# Source:
# http://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
#ENGLISH_FREQUENCIES = {
#'E': .1202, 'T': .0910, 'A': .0812, 'O': .0768, 'I': .0731, 'N': .0695,
#'S': .0628, 'R': .0602, 'H': .0592, 'D': .0432, 'L': .0398, 'U': .0288,
#'C': .0271, 'M': .0261, 'F': .0230, 'Y': .0211, 'W': .0209, 'G': .0203, 
#'P': .0182, 'B': .0149, 'V': .0111, 'K': .0069, 'X': .0017, 'Q': .0011, 
#'J': .0010, 'Z': .0007,
#}

       # for byte in range(0,255):
            # plaintext = ''
            # score = 0
            # for x in line:
                # #nextchar = chr(ord(x) ^ ord(alphabet[j]))
                # nextchar = chr(ord(x) ^ byte)
                # plaintext += nextchar
                # #if nextchar.upper() in ENGLISH_FREQUENCIES:
                # #    score = score + (ENGLISH_FREQUENCIES[nextchar.upper()])
                # if score > highscore: 
                    # highscore = score
            # if 'ing' in plaintext:
                # print plaintext
            # #if score == highscore:
            # #    print 'HIGH SCORE:',score,'   ',plaintext
            # # if score > 3:
               # # print 'HIGH SCORE:',score,'   ',plaintext