from Crypto.Hash import SHA256
import random, string


def hashArbitraryInput(input):
    print("Arbitrary input: " + input)
    bytesInput = str.encode(input) # converts string input into bytes
    h = SHA256.new()
    h.update(bytesInput)
    print("Resulting digest: ", end = "")
    return h.hexdigest()

def main():
    print(hashArbitraryInput("hello"))
    print(hashArbitraryInput("iello")) # iello has hamming distance of 1 bit with hello

    print(hashArbitraryInput("a"))
    print(hashArbitraryInput("b")) # a has hamming distance of 1 bit with b

    print(hashArbitraryInput("BOB"))
    print(hashArbitraryInput("BOA"))

if __name__ == '__main__':
    main()
    