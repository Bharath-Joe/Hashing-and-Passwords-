from Crypto.Hash import SHA256
import random, string
import datetime

from numpy import binary_repr

def hashArbitraryInput(input):
    bytesInput = str.encode(input) # converts string input into bytes
    h = SHA256.new()
    h.update(bytesInput)
    return h.hexdigest()

def modifyDigest(digestValue, modVal, length):
    modVal = int(modVal, 16)
    finalBits = ""
    for val in digestValue:
        fourBitValue = '{:04b}'.format(int(val, 16))
        finalBits += fourBitValue
    finalBits = int(finalBits, 2)
    binaryAfterMod = bin(finalBits % modVal).replace("0b","").zfill(length)
    return binaryAfterMod

def generateMessage():
    res = ''.join(random.choices(string.ascii_letters, k = 16))
    return res

def findCollision(modVal, length):
    myDict = {}
    while(True):
        someInput = generateMessage()
        truncatedDigest = modifyDigest(hashArbitraryInput(someInput), modVal, length)
        if truncatedDigest in myDict.keys():
            return myDict[truncatedDigest], truncatedDigest, someInput, len(myDict.keys())
        else:
            myDict[truncatedDigest] = someInput
            continue


def main():
    # print(hashArbitraryInput("hello"))
    # print(hashArbitraryInput("iello")) # iello has hamming distance of 1 bit with hello

    # print(hashArbitraryInput("a"))
    # print(hashArbitraryInput("b")) # a has hamming distance of 1 bit with b

    # print(hashArbitraryInput("BOB"))
    # print(hashArbitraryInput("BOA")) # BOB has hamming distance of 1 bit with BOA

    hexString = 'ff'
    addedVal = '3'
    for i in range(8, 52, 2):
        if i % 4 != 0:
            hexString = addedVal + hexString
        if i % 4 == 0 and i != 8:
            hexString = hexString.replace("3", "f", 1)
        print("Num of bits are: ", i)
        start_time = datetime.datetime.now()
        print(findCollision(hexString, i))
        end_time = datetime.datetime.now()
        print("Time elapsed: ", end_time - start_time)
        print("----")


if __name__ == '__main__':
    main()
    