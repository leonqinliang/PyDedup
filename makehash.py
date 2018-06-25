#! /usr/local/bin/python3

import hashlib
import sys
import codecs

def main():
    testFileName = 'testfile.txt'

    testFile = codecs.open(testFileName, 'rU', 'utf-8')

    for singleLine in testFile:
        if singleLine[-1:] == '\n':
            singleLine = singleLine [:-1]

        print (singleLine)
        print (hashlib.md5(singleLine.encode('utf-8')).hexdigest())

    testFile.close()

if __name__ == '__main__':
    main()