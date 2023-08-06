import os
class OpenFile:
    def __init__(self,name):
        self.file = name
    @property
    def readlines(self,mode='r'):
        with open(self.file,mode) as file:
            return file.readlines()
    @property
    def readline(self,mode='r'):
        with open(self.file,mode) as file:
            return file.readline()
    @property
    def read(self,mode='r'):
        with open(self.file,mode) as file:
            return file.read()
    def write(self,writes,mode='w'):
        with open(self.file,mode) as file:
            file.write(writes)
    def append(self,writes,mode='a'):
        with open(self.file,mode) as file:
            file.write(writes)
    def delFile(self):
        os.remove(self.file)

import zipfile
def zipFile(path,name):
    with zipfile.ZipFile(name,'w') as target:
        for i in os.walk(path):
            for n in i[2]:
                target.write(''.join((i[0],'/',n))) 
