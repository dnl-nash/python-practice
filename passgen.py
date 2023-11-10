from random import randint as ri
try:
	from pyperclip import copy
	clipcopy=True
except ModuleNotFoundError:
	clipcopy=False
def genpass(len,clipcopy=clipcopy):
	ctr=0
	password=''
	while(ctr<len):
		passchr=chr(ri(0,255))
		password+=passchr
		ctr=ctr+1
	if(clipcopy):
		copy(password)
	return password
genpass(512)
