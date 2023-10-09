from random import randint as ri
calls=[]
ltrs=['b','i','n','g','o']
while 1:
    callltr=ltrs[ri(0,len(ltrs)-1)]
    match(callltr):
        case "b":
            nummin=1
            nummax=15
        case "i":
            nummin=16
            nummax=30
        case "n":
            nummin=31
            nummax=45
        case "g":
            nummin=46
            nummax=60
        case "o":
            nummin=61
            nummax=75
    callnum=ri(nummin,nummax)
    print(callltr)
    print(callnum)
    calls.append(str(callltr)+"\n"+str(callnum))
    cmd=input()
    match(cmd):
        case "c":
            calls.clear()
            print("calls cleared")
        case "s":
            print("called so far: ")
            for i in calls:
                print(i)
        case "?":
            print("Available Commands: question mark, ?: Show help. c: Clear List of calls. s: Show calls made so far. Any unrecognized command will continue generation.")
