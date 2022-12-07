import numpy as np

class Hit:
    def __init__(self,modulo,sensore,tempo):
        self.modulo=modulo
        self.sensore=sensore
        self.tempo=tempo
    def __lt__(self,other):
        return self.tempo < other.tempo

class Event:
    def __init__(self):
        self.nhit=0
        self.tstart=np.inf
        self.tstop=-np.inf
        self.durata=np.inf
        self.a_Hit=np.empty(0)
    def aggiungi_hit(self,Hit):
        if self.nhit==0:
            self.tstart=Hit.tempo
        self.nhit=(self.nhit)+1
        self.tstop=Hit.tempo
        self.durata=self.tstop-self.tstart
        self.a_Hit=np.append(self.a_Hit,Hit)
