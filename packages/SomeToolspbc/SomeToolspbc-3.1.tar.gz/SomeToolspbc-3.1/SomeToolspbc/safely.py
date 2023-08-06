from sys import getsizeof
from SomeToolspbc.math import strdel

BIT = 1
B = BIT * 8
KB = B * 1024
MB = KB * 1024
GB = KB * 1024
TB = GB * 1024

pyStrA = 50
pyInt1 = 28
pyInt0 = 24
pyNone = 16

data = None

class reglist:
    def init(self,name,size=1024*1024*3):
        global data
        self.list = []
        self.size = size
        self.name = name
        self.now = 0
        data.append(f"{self.name} is init")
        if getsizeof(self.list) > self.size:
            raise ValueError(f"the {self.size} is too small!\
the size must bigger than {getsizeof(self.list)}")
    def getHave(self):
        return self.size - getsizeof(self.list)
    def append(self,a):
        self.list.append(a)
        self.now += 1
    def display(self):
        for i in range(len(self.list)):
            print(f'line {i}:',self.list[i])
    def clearMost(self):
        if getsizeof(self.list) > self.size:
            data.append(f'ERROR in regs,used space bigger than {self.size} ,so start clear {self.name}')
            while getsizeof(self.list) > self.size:
                del self.list[0]
                self.now -= 1
                if self.now < 0:
                    print("ERROR:size too small")
                    sys.exit(1)
                
            data.append(f'end clear {self.name}')
    def ch(self,a,thing):
        if a >= self.now:
            data.append(f'ERROR:no {a}')
class regdict:
    def init(self,name,size=1024*1024*3):
        global data
        self.list = {}
        self.size = size
        self.name = name
        data.append(f"{self.name} is init")
    def getHave(self):
        return self.size - getsizeof(self.list)
    def append(self,a,name):
        self.list[name]=a
    def display(self):
        for i in self.list:
            print(f'line {i}:',self.list[i])
    def clearMost(self):
        if getsizeof(self.list) > self.size:
            data.append(f'ERROR in regs,used space bigger than {self.size} ,so start clear {self.name}')
            while getsizeof(self.list) > self.size:
                for i in self.list:
                    del self.list[i]
                    if getsizeof(self.list) <= self.size:break
                #    print("ERROR:size too small")
                #    sys.exit(1)
            data.append(f'end clear {self.name}')
    def ch(self,a,thing):
        self.list[a]=thing
        
class regthing:
    def init(self,name,size=1024*1024*3):
        global data
        self.list = None
        self.size = size
        self.name = name
        self.now = 0
        data.append(f"{self.name} is init")
    def getHave(self):
        return self.size - getsizeof(self.list)
    def display(self):
        print(self.list)
    def clearMost(self):
        if getsizeof(self.list) > self.size:
            data.append(f'ERROR in regs,used space bigger than {self.size} ,so start clear {self.name}')
            if type(self.list) == int:
                self.list = -1
            elif type(self.list) == str:
                while getsizeof(self.list) > self.size:
                    self.list = strdel(self.list,[0])
            else:
                self.list = None
            data.append(f'end clear {self.name}')
    def ch(self,thing):
        self.list = thing
data=reglist()
data.init('data')
