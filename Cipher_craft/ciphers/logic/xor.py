def encryptDecrypt(xorKey,inpString):
    try: 
        length = len(inpString)
        for i in range(length):
            inpString = (inpString[:i] +chr(ord(inpString[i]) ^ ord(xorKey)) +inpString[i + 1:])
            # print(inpString[i], end="")
        return inpString
    except:
        return "#"