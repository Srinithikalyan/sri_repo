"""
File handling
"""
print "*****************File handling*******************"

import os
try:

    os.mkdir('test')      #creating new directory
    os.chdir('test')      #changing into created directory
    f = open("test.txt",'w')
    f.write("hello world\n")   #file writing
    f.write("This code is for writing text into file\n")
    print "Writing operation successful"
    f.close()
    with open("test.txt",'r') as f:
        r = f.read(7); print r
        re = f.readlines()
        for line in re:
            words = line.split()
            print words    
    f.close()
except OSError:
    print "The File already exists"

