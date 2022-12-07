
# //// Imports
import os
import sys
import platform

# ========== Global SRT ========== ** Global Functions and variables used in every Program at the start

class G1:  # .. Global Functions
    def SystemOS():  # .... Determines user Operating System, returns value
        if sys.platform == 'win32':
            return 0
        elif sys.platform == 'linux':
            return 1
        elif sys.platform == 'darwin':
            return 2
        else:
            return 3
    def GlobalSlash(OSnum): # .... Determines whether a '/' or a '\' is used when handling file structures
        if OSnum == 0: # .. win32
            return '\\'
        elif OSnum >= 1: # .. linux, macOS, unknown
            return '/'
    def MainPath(): # .... Gets Directory Path of Executable
        if getattr(sys, 'frozen', False):
            Path = os.path.dirname(sys.executable)
            return [0,Path]
        elif __file__:
            Path = os.path.dirname(__file__)
            return [1,Path]
        else:
            return [2,""]
    def GlobalArch(): # .... Global System Architecture
        arch = platform.machine()
        if platform.machine().find('64') >= 1:
            return 0
        else:
            return 1
    def GetSysInfo():
        print(G3.MSG[0])
        D.Dprint(G2.OS,0,[1,2,3,4],"") # Print OS Information
        D.Dprint(G2.Garch,1,[6,7,8],"") # print System Architecture
        D.Dprint(G2.MPath[0],2,[9,10,11],G2.MPath[1]) # Print Main Filepath

class G2: # .. Global Variables
    # // System
    DMODE = 1 # DEBUG Mode. 0 == No Debug, 1 == Basic Debug, 2 == Full Debug
    OS = G1.SystemOS() # .. OS Name, expressed as integer
    GS = G1.GlobalSlash(OS) # .. OS Global Slash, '/' or '\'
    MPath = G1.MainPath() # .. Filepath of Executable
    Garch = G1.GlobalArch() # .. Global Architecture of System (64/32 bit)


class G3: # .. Global Messages and Errors
    # // Messages
    MSG = {
    # System info
    0 : "System Information:",
    1 : "OS:",
    2 : "win32",
    3 : "linux",
    4 : "darwin",
    5 : "Unknown OS",
    6 : "Architecture:",
    7 : "64-bit",
    8 : "32-bit",
    9 : "System Path",
    10 : "(exe):",
    11 : "(main.py):",
    12 : "",
    13 : "",
    14 : "",
    15 : "",
    16 : "",
    17 : "",
    18 : "",
    19 : "",
    20 : "",
    21 : "",
    22 : "",
    23 : "",
    24 : "",
    25 : "",
    26 : "",
    27 : "",
    28 : "",
    29 : "",
    30 : ""
    # Can keep adding, stops at arbitrary point.
    }

    # // Errors
    ERR = {
    # System Errors
    0 : "ERROR : No Operating System Type Detected",
    1 : "ERROR : Cannot Determine 32-bit or 64-bit System",
    2 : "ERROR : Cannot find MainPath"
    }

# ========== Global END ==========


# ========== DEBUG SRT ==========

class D: # .. Debug Class
    def Dprint(MainVal,valEM,MsgLst,ext):
        if MainVal == (len(MsgLst)-1):
            print(G3.ERR[valEM]) # .... Prints Fatal Error Values
            exit() # .... Closes program, as any ERROR in this category should stop the Program
        else:
            print(G3.MSG[MsgLst[0]],G3.MSG[MsgLst[MainVal+1]],ext) # .... Prints first Message in selected available Dictionary items, then the Main Message value, and optional external Message
    def DEBUG1(list,section): # .... Standard Debug Function
        print("==========",section,"SRT","==========")
        for i in list:
            print(i)
        print("==========",section,"END","==========")
    def DEBUG2(): # .... Advanced Debug Function
        pass

# ========== DEBUG END ==========


# ========== Functions SRT ========== ** Class Functions for Project, where most of the work goes

# //// A1 SRT
class A1:  # .. Example Class
    def Func1():  # .... Example Function
        pass
# //// A1 END

# ========== Functions END ==========

# ========== Run Program SRT ==========

class Run:
    def MainRun(): # .... Main Program Run
        G1.GetSysInfo() # .. Start with SysInfo Function to start Program
    def TestRun(): # .... Test Function, for experimenting and hardcore debug
        pass


# ========== Run Program END ==========

Run.MainRun()
