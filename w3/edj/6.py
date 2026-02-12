class birbale():
    def __init__(self , dlina , shirina):
        self.dlina = dlina
        self.shirina = shirina
     
    def hz(self):
        return self.dlina * self.shirina
    
dlina, shirina = map(int, input().split())
blmeim = birbale(dlina , shirina)
print(blmeim.hz())
    
