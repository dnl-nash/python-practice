import httpx
import bs4
import os
import hashlib
def dlfile(tgtlink,output=None):
    '''
    Downloads a file using httpx and bs4
    Parameters:
    tgtlink: 
    list in the format ['path to resource including final /','filename']
    output:
    string for output file name, default None. If None, uses index.html'''
    if (len(tgtlink)==1):
        tgtlink.append("index.html")
    if output is None:
        output=tgtlink[1]
    if(os.path.isfile(output)):
        print(output," already exists.")
        return(2)
    else:
        url=''
        url=url.join(tgtlink)
        print("Downloading",output)
        file=open(output,"wb")
        with httpx.stream("GET", url) as chunk:
            for data in chunk.iter_bytes():
                file.write(data)
        file.close()
def verifyfile(tgtlink,checksum=hashlib.sha512,checksumext='sha512',output=None):
    '''Verifies a given file
    Parameters:
    tgtlink: 
    list in the format ['path to resource including final /','filename']
    checksum:
    hashlib checksum function to hash with, defaults to hashlib.sha512
    checksumext:
    extension of the file containing the source checksum
    output:
    where to save the source checksum file to during verification'''
    if (len(tgtlink)==1):
        tgtlink.append("index.html")
    if output is None:
        output=tgtlink[1]+"."+checksumext
    tgtlink.pop()
    tgtlink.append(output)
    dlfile(tgtlink,output)
    checksumfile=open(output,"rt")
    for filetoverify in checksumfile.readlines():
        checksumline=filetoverify.split(" ")
        checksumtxt=checksumline[0]
        filename=checksumline[1]
        filetoverify=open(output.strip("."+checksumext),"rb")
        srcchecksum=hashlib.file_digest(filetoverify,checksum).hexdigest()
        filetoverify.close()
        if(srcchecksum==checksumtxt):
            print('checksum matches!')
        else:
            print('checksum does not match')
