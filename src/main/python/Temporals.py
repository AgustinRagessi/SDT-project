class Temporals:
    _tempList = []
    _temp = 0
    
    @property
    def tem(self):
        Temporals._temp += 1
        self._tempList.append(Temporals._temp)
        return f't{Temporals._tempList[-1]}'
    
    @property
    def prevTem(self):
        return f't{Temporals._tempList[-2]}'
    
    @property
    def actualTem(self):
        return f't{Temporals._tempList[-1]}'