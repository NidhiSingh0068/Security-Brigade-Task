# Task 8

# Please write a program to compress and decompress the string "Music industry hails passage of the Music Modernization Act".


#######################################################################################################################################################################

import sys
import gzip

s = b"Music industry hails passage of the Music Modernization Act"
# Compressing
s = gzip.compress(s)
print("Compressed String : ", s)
res = sys.getsizeof(str(s))
print("The length of Compressed string in bytes : " + str(res))

# Decompressing
t = gzip.decompress(s)
print("Decompressed String : ", t)
res = sys.getsizeof(str(t))
print("The length of Decompressed string in bytes : " + str(res))
