class Intervallo:
    def __init__(self, intDistanzaGradi, intDistanzaSemitoni,intOttave=0):
        self.dg = intDistanzaGradi
        self.ds = intDistanzaSemitoni
        self.do = intOttave
    def __str__(self):
        return "Intervallo "+ str(self.dg)+" gradi e "+str(self.ds)+" semitoni"
    def __repr__(self):
        return self.__str__()
    
    @property
    def maggiore(self):
        maggiore = [secondaM, terzaM, sestaM, settimaM]
        return (self.dg, self.ds) in maggiore
    @property
    def minore(self):
        minore = [secondam,terzam,sestam,settimam]
        return (self.dg, self.ds) in minore
    @property
    def giusto (self):
        giusto = [unisonoG,quartaG,quintaG,ottavaG]
        return (self.dg, self.ds) in giusto
    
    @property
    def consonante (self):
        punteggio = 0
        if self.maggiore or self.minore or self.giusto:
            punteggio += 10
        if self.ds == 3:
            #nessun punto per gli unisoni!
            punteggio = 0
        if self.ds == 2:
            punteggio -=4
        if self.ds == 1:
            punteggio -= 10
        if self.ds == 11:
            punteggio -= 10
        return punteggio/10
semitono    = (0,1)
unisonoG    = (0,0)
secondam    = (1,1)
secondaM    = (1,2)
terzam      = (2,3)
terzaM      = (2,4)
quartaG     = (3,5)
quintaG     = (4,7)
sestam      = (5,8)
sestaM      = (5,9)
settimam    = (6,10)
settimaM    = (6,11)
ottavaG     = (0,0,1)
