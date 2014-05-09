class Intervallo:
    def __init__(self, intDistanzaGradi, intDistanzaSemitoni):
        self.dg = intDistanzaGradi
        self.ds = intDistanzaSemitoni
    def __str__(self):
        return "Intervallo "+ str(self.dg)+" gradi e "+str(self.ds)+" semitoni"
    def __repr__(self):
        return self.__str__()
    
    @property
    def maggiore(self):
        maggiore = [(1,2),(2,4),(5,9),(6,11)]
        return (self.dg, self.ds) in maggiore
    @property
    def minore(self):
        minore = [(1,1),(2,3),(5,8),(6,10)]
        return (self.dg, self.ds) in minore
    @property
    def giusto (self):
        giusto = [(0,0),(3,5),(4,7),(7,12)]
        return (self.dg, self.ds) in giusto
    
    @property
    def consonante (self):
        punteggio = 0
        if self.maggiore or self.minore or self.giusto:
            punteggio += 10
        if self.ds == 1:
            punteggio -= 8
        if self.ds == 11:
            punteggio -=5
        return punteggio/10
