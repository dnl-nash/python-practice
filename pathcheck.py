from pathlib import Path
from sys import argv
if(len(argv)-1<=0):
    print("Enter Path to Check")
    pc=input()
    p=Path(pc)
else:
    p=Path(sys.argv[1])
if(p.exists()):
    exit(0)
else:
    exit(1)
