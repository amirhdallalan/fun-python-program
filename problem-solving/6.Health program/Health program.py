class kelas():
    def __init__(self, num):
        self.num = num
    def Sen(self):
        self.sen = input().split(" ")
    def Ghad(self):
        self.ghad = input().split(" ")
    def Vazn(self):
        self.vazn = input().split(" ")
    def ave(self, l):
        sum = 0
        for i in range(0,len(l)):
            sum += int(l[i])
        return (sum/len(l))
    def read(self):
        self.Sen()
        self.Ghad()
        self.Vazn()
    def Out(self):
        print(self.ave(self.sen))
        print(self.ave(self.ghad))
        self.av = self.ave(self.vazn)
        print(self.av)

a = kelas(int(input()))
a.read()
b = kelas(int(input()))
b.read()
a.Out()
b.Out()
if a.av>b.av:
    print('A')
elif a.av<b.av:
    print('B')
else:
    print('Same')