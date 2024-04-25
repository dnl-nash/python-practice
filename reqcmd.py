from shutil import which
from sys import argv
def require(cmd,fatal=True):
    if which(cmd):
        return 0
    else:
        if(fatal):
            exit(2)
        else:
            return 1
if(len(argv)-1<=0):
    print("Enter command to check")
    cmd=input()
else:
    cmd=argv[1]
stat=require(cmd)
exit(stat)
