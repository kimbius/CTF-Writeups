import hashlib

def split_str(s):
    return [c for c in s]

def hashmd5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

Password = []
XPin = []
CorrectPassword = "RPC@_CYB3RC10B"
CPass = split_str(CorrectPassword)
key = []
CR = ["Correct"]
print ("\nTo open this box you shoud enter the Pin that make the correct password. \n\nPin a is the alphabet.\nPin b is number and symbol.\n\nExample Pin : a10 b15\n ")

def APASS (Pin,Password):
    A = ['c', 'J', 'i', 'Z', 'x', 'a', 'K', 'N', 'Y', 'y', 'S', 'L', 'E', 'n', 'h', 'o', 'j', 'G', 'q', 'O', 'f', 'U', 'g', 'C', 'k', 'I', 'p', 'T', 'P', 'w', 'l', 's', 'V', 'm', 'b', 'M', 'u', 'D', 't', 'B', 'e', 'r', 'A', 'H', 'd', 'X', 'W', 'Q', 'R', 'F', 'z', 'v']
    AP = A[Pin]
    Password.append(AP)
    print ("Password : ",end ="")
    for i in Password:
        print(i, end = "")
    #print ("\n")
    return Password
    
def BPASS (Pin,Password):
    B = ['4', '*', '1', '@', '%', '#', '!', '5', '6', '-', '$', '9', '7', '_', '^', '0', '8', '&', '3', '2']
    BP = B[Pin]
    Password.append(BP)
    print ("Password : ",end ="")
    for i in Password:
        print(i, end = "")
    #print ("\n")
    return Password

def CheckP (Password,key):
    if Password == CPass:
        key.append("Correct")
        f = "".join(XPin)
        flag = hashmd5(f)
        print ("\n\nCorrect!!! this is your flag : RPCACTF{%s}"%(flag))
        return key
        
while key != CR:
    
    pin1 = str(input("Please enter the pin : "))
    Pin = int(pin1[1:])

    print(Pin)
    
    if Pin >= 0 :
        print ("*ERROR*")
        break
    else :
        if pin1[0] == "a":
            APASS(Pin,Password)
            XPin.append(pin1)
            print ("\nYour pin : " ,end = "")
            for i in XPin:
                print(i ,end="")
            print ("\n")
        
        elif pin1[0] == "b":
            BPASS(Pin,Password)
            XPin.append(pin1)
            print ("\nYour pin : " ,end = "")
            for i in XPin:
                print(i ,end="")
            print ("\n")
        else:
                print ("*ERROR*")
                break
        CheckP(Password,key)