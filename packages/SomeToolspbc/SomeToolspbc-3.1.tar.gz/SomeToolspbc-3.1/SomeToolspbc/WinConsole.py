import ctypes,sys,pygame

pygame.mixer.init()

BLACK=0x0
BLACK_BLUE=0x1
BLACK_GREEN=0x2
BLACK_BLUE=0x3
BLACK_RED=0x4
BLACK_PURPLE=0x5
BLACK_YELLOW=0x6
BLACK_WHILE=0x7
BLACK_BLACK_WHITE=0x8
WATER=0x9
WHILE_GREEN=0xa
WHILE_BLUE=0xb
WHILE_RED=0xc
WHILE_PURPLE=0xd
WHILE_YELLOW=0xe
WHILE=0xf

#help(pygame.mixer.Sound)
class Music(pygame.mixer.Sound):
    pass

class WinConsoleError(Exception):
    def __init__(self,raiseStr,where):
        self.strs = raiseStr
        self.wh = where
    def __str__(self):
        return f'<{self.wh}>{self.strs}'

DLL = ctypes.CDLL("consoleW.dll",winmode=0)

def setXY(x,y):
    if type(x)!=int or type(y)==int:
        raise WinConsoleError("you gived not is int",'getXY')
    DLL.setxy(x,y)
def setColor(color):
    DLL.setColor(color)
def cout(*a):
    for i in a:
        sys.stdout.write(i)
    
#DLL.setColor(0x8)
#DLL.setxy(5,5)
#print('f',end='')
#input()
#DLL.setxy(5,5)
#print('d',end='')
#input()
