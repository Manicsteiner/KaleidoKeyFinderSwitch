import os,sys,struct

def main(file):
    if not os.path.exists(file):
        print("File not exist")
        return
    file_size = os.path.getsize(file)
    data = open(file, 'rb')
    totalsuspects = 0
    totalmarked = 0
    for i in range (file_size-14):
        if(data.read(1) == b"\x00"):
            pin = data.tell()
            suspect = True
            num_s = False
            upp_s = False
            low_s = False
            for i in range (13):
                tmp = data.read(1)[0]
                if not (isascii(tmp)):
                    suspect = False
                    break
                if not (isnotnumber(tmp)):
                    num_s = True
                if not (isnotuppercase(tmp)):
                    upp_s = True
                if not (isnotlowercase(tmp)):
                    low_s = True
            strMark = ""
            if (num_s and (low_s or upp_s) and suspect):
                strMark = " Marked"
                totalmarked += 1
            if (suspect):
                data.seek(pin)
                print("Destination " + str(pin) + " " + cstr(b'' + data.read(13)) + strMark)
                totalsuspects += 1
            data.seek(pin)
    print("Complete! Totaly " + str(totalsuspects) + " suspects and " + str(totalmarked) + " marked as highly suspicious.")

def cstr(s):
    p = "{}s".format(len(s))
    s = struct.unpack(p,s)[0]
    return str(s.replace(b"\x00",b""),encoding = "sjis",errors = "ignore")
    
def isascii(s):
    if(s>=48 and s<=57 or s>=64 and s<=90 or s>=97 and s<=122):
        return True
    else:
        return False

def isnotuppercase(s):
    if(s>=64 and s<=90):
        return False
    else:
        return True

def isnotlowercase(s):
    if(s>=97 and s<=122):
        return False
    else:
        return True

def isnotnumber(s):
    if(s>=48 and s<=57):
        return False
    else:
        return True

if __name__ =="__main__":
    if len(sys.argv) < 2 :
        exit()
    files=[]
    files=sys.argv[1:]
    for file in files:
        main(file)
    