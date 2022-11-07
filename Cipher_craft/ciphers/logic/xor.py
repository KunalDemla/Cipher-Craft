def encryptDecrypt(xorKey,inpString):
    length = len(inpString)
    for i in range(length):
        inpString = (inpString[:i] +chr(ord(inpString[i]) ^ ord(xorKey)) +inpString[i + 1:])
        # print(inpString[i], end="")
    return inpString