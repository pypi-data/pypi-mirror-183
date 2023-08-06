import tkinter,SomeToolspbc.math,copy


class windows:
    def __init__(self,w,h,x=0,y=0):
        self.win = tkinter.Tk()
        self.win.geometry(SomeToolspbc.math.add(str(w),'x',str(h),'+',str(x),'+',str(y)))
        self.have = {}
    def add(self,obj,name=None):
        if name == None:
            self.have[len(self.bt)] = copy.copy(obj)
        else:
            self.have[name] = copy.copy(obj)
    def loop(self):
        self.win.mainloop()

class text:
    def __init__(self,txt,target):
        self.mine = tkinter.Label(target,text=txt)
    def ret(self):
        return self.mine

class button:
    def __init__(self,txt,target,command=None):
        self.mine = tkinter.Button(target,text=txt,command=command)
    def ret(self):
        return self.mine
