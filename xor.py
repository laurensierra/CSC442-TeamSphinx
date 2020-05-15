###########################
#Name: Lauren Gilbert
#Date: May 5, 2020
#Version: Python 2
#Notes:this program takes ciphertext and plaintext and changes it to the other using a key that is in the file
###########################


from sys import stdin, stdout
import sys 


#read key from file that we open through the program 
#key file is in same directory as program
key_file = open('key.bin', 'rb').read()

#input text file as byte array
text = sys.stdin.read()
byteArray = bytearray()
i=0
#xor with each value in key with value that goes in input array and store result in binary array
while(i < len(key_file)):
    #xor one byte at a time
    xor = ord(text[i]) ^ ord(key_file[i])
    #bytearray from the key and text that have been compared
    byteArray.append(xor)
    i += 1

#send bytearray to stdout
sys.stdout.write(byteArray)
