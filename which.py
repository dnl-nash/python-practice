#!/usr/bin/python
from sys import argv
from sys import platform as plat
from sys import exit
from os import environ, listdir, path
def findcmd(command,quiet=True):
    '''Searches for a given command in your path
    If quiet is set to true, the output will not be displayed
    Input:
        A command name
    Returns/outputs:
        A list of commands with path names
    Error/abnormal Conditions:
        raises AttributeError if the PATH environment variable has no valid entries
        raises FileNotFoundError if the command was not found
        raises LookupError if no command was supplied
    '''
    foundcmds=[]
    paths=environ.get("PATH")
    if(plat=="linux"):
        pathsep=":"
        dirsep="/"
    elif(plat=="windows"):
        pathsep=";"
        dirsep="\\"
    if(paths==None):
        raise AttributeError("Cannot find any entries in PATH environment variable.")
    else:
        paths=paths.split(pathsep)
    for dir in paths:
        if not (path.exists(dir)):
            paths.remove(dir)
        filetosearch=''
        filetosearch=filetosearch.join([dir,dirsep,command])
        if path.exists(filetosearch):
            foundcmds.append(filetosearch)
    if(len(foundcmds)==0):
        raise FileNotFoundError(command," not found")
    if(quiet==False):
        for cmd in (foundcmds):
            print(cmd)
    return(foundcmds)
def main():
    try:
        mycmd=argv[1]
    except IndexError:
        raise LookupError("No Command Supplied")
    findcmd(mycmd)
