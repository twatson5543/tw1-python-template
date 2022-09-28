
# //// Imports
import os
import sys

# ========== Global SRT ========== ** Global Functions and variables used in every Program at the start

class G1:  # .. Global Functions
    def SystemOS():  # .... Determines user Operating System, returns value
        if sys.platform == 'win32':
            return 1
        elif sys.platform == 'linux':
            return 2
        elif sys.platform == 'darwin':
            return 3
        else:
            return 4
    def GlobalSlash(OSnum): # .... Determines whether a '/' or a '\' is used when handling file structures
        if OSnum == 1: # .. win32
            return '\\'
        elif OSnum >= 2: # .. linux, macOS, unknown
            return '/'
    def MainPath(): # .... Gets Directory Path of Executable
        Path = str()
        if getattr(sys, 'frozen', False):
            Path = os.path.dirname(sys.executable)
        elif __file__:
            Path = os.path.dirname(__file__)
        return Path
    def newfunc():
        pass

class G2: # .. Global Variables
    # // System
    OS = G1.SystemOS() # .. OS Name, expressed as integer
    GS = G1.GlobalSlash(OS) # .. OS Global Slash, '/' or '\'
    MPath = G1.MainPath() # .. Filepath of Executable


class G3: # .. Global Messages and Errors
    # // Messages
    MSG = {
    # System info
    0 : "System Information:",
    1 : "Windows",
    2 : "Linux",
    3 : "MacOS",
    4 : "Unknown",
    5 : "x64",
    6 : "x86"
    }

    # // Errors
    ERR = {
    # System Errors
    0 : "Error : No Operating System Type Detected",
    1 : "Error : Cannot Determine 32-bit or 64-bit System",
    2 : "Error : "
    }

# ========== Global END ==========


# ========== DEBUG SRT ==========

class D: # .. Debug Class
    def DEBUG1(): # .... Standard Debug Function
        pass
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
        pass
    def TestRun(): # .... Test Function, for experimenting and hardcore debug
        print(G3.MSG[5])

# ========== Run Program END ==========

Run.TestRun()
