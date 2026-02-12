class area():
    def __init__(self,dlina):
        self.dlina = dlina

    def hz(self):
        return self.dlina * self.dlina
    
n = int(input())
blmeim = area(n)
print(blmeim.hz())