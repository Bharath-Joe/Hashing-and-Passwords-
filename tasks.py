from Crypto.Hash import SHA256
import random, string


def hashArbitraryInput(input):
    # print("Arbitrary input: " + input)
    bytesInput = str.encode(input) # converts string input into bytes
    h = SHA256.new()
    h.update(bytesInput)
    # print("Resulting digest: ", end = "")
    return h.hexdigest()

def modifyDigest(digestValue):
    # truncate to 16 bits
    return digestValue[0:4]

def generateMessage():
    res = ''.join(random.choices(string.ascii_letters, k = 16))
    return res

def findCollision():
    myDict = {}
    while(True):
        someInput = generateMessage()
        someInput2 = generateMessage()
        if someInput != someInput2:
            firstDigest = modifyDigest(hashArbitraryInput(someInput))
            myDict[someInput] = firstDigest
            secondDigest = modifyDigest(hashArbitraryInput(someInput2))
            myDict[someInput2] = secondDigest
            for key in myDict.keys():
                for key2 in myDict.keys():
                    if key != key2 and myDict[key] == myDict[key2]:
                        return key, key2
        else:
            continue


def main():
    # print(hashArbitraryInput("hello"))
    # print(hashArbitraryInput("iello")) # iello has hamming distance of 1 bit with hello

    # print(hashArbitraryInput("a"))
    # print(hashArbitraryInput("b")) # a has hamming distance of 1 bit with b

    # print(hashArbitraryInput("BOB"))
    # print(hashArbitraryInput("BOA")) # BOB has hamming distance of 1 bit with BOA

    # print(generateMessage())
    val, val1 = findCollision()
    print(hashArbitraryInput(val))
    print(hashArbitraryInput(val1))

if __name__ == '__main__':
    main()
    