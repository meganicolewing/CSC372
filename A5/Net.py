from random import random
class Net:
    def __init__(self):
        self.B = 0.02
        self.E = 0.03
        self.ABtEt = 0.97
        self.ABtEf = 0.92
        self.ABfEt = 0.36
        self.ABfEf = 0.03
        self.JAt = 0.85
        self.JAf = 0.07
        self.MAt = 0.69
        self.MAf = 0.02

    def And(self,burglary=bool,earthquake=bool,alarm=bool,john=bool,mary=bool) -> float:
        prob = 1
        if burglary:
            prob = prob*self.B
        else:
            prob = prob*(1-self.B)
        if earthquake:
            prob = prob*self.E
        else:
            prob = prob*(1-self.E)
        temp_prob = 1
        if burglary:
            if earthquake:
                temp_prob=self.ABtEt
            else:
                temp_prob=self.ABtEf
        else:
            if earthquake:
                temp_prob=self.ABfEt
            else:
                temp_prob=self.ABfEf
        if not alarm:
            temp_prob = 1-temp_prob
        prob = prob*temp_prob
        temp_prob = 1
        if alarm:
            temp_prob = self.JAt
        else:
            temp_prob=self.JAf
        if not john:
            temp_prob=1-temp_prob
        prob = prob*temp_prob
        temp_prob = 1
        if alarm:
            temp_prob = self.MAt
        else:
            temp_prob=self.MAf
        if not mary:
            temp_prob=1-temp_prob
        prob = prob*temp_prob
        return prob
        
    def pBreakin(self)->bool:
        rand = random()
        return rand<self.B
    
    def pEarthquake(self)->bool:
        rand=random()
        return rand<self.E
    
    def pAlarm(self,breakin=bool,earthquake=bool)->bool:
        rand=random()
        if breakin:
            if earthquake:
                return rand<self.ABtEt
            return rand<self.ABtEf
        elif earthquake:
            return rand<self.ABfEt
        return rand<self.ABfEf
    
    def pJohn(self,alarm=bool)->bool:
        rand=random()
        if alarm:
            return rand<self.JAt
        return rand<self.JAf
    
    def pMary(self,alarm=bool)->bool:
        rand=random()
        if alarm:
            return rand<self.MAt
        return rand<self.MAf

    def priorSample(self)-> list[bool]:
        sample = []
        sample.append(self.pBreakin())
        sample.append(self.pEarthquake())
        sample.append(self.pAlarm(sample[0],sample[1]))
        sample.append(self.pJohn(sample[2]))
        sample.append(self.pMary(sample[2]))
        return sample