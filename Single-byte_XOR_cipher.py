ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
wordparts = ['ing','er','or','ess','ist','ast','ian','ant',
'oi','io','ll','to','on','ir','ri','uo','ou','ent','ee',
'ic','oo','ic','man','woman','person','eur','tion','nce',
'ty','ry','ism','ics','ure','ss','an','en','ac','es']
ciphertext_decoded = ciphertext.decode("hex")
#print 'ciphertext:', ciphertext
#print 'ciphertext_decoded: ', ciphertext_decoded
for j in range(0,len(alphabet)):
    plaintext = ''
    score = 0
    for x in ciphertext_decoded:
        plaintext = plaintext + chr(ord(x) ^ ord(alphabet[j]))
        for x in wordparts:
            if plaintext.endswith(x):
                score = score + 1
    if score > 3:
        print 'HIGH SCORE:',score,'   ',plaintext
    #print plaintext