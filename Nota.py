from Exceptions import *
from Intervallo import Intervallo
class Nota:
    scala = {"c": 0,"d":2,"e":4,"f":5,"g":7,"a":9,"b":11}
    note = ["c","d","e","f","g","a","b"]
    alterazioni = {-2 : "eses", -1: "es",0:"",1:"is",2:"isis"}
    numSemitoni = 12
    
    def __init__(self, strNome, intAlterazione, intOttava = 4):
        if strNome not in self.scala:
            raise NotaException("Il nome deve appartenere a "+ str(nomiNote))
        self.nome = strNome
        if intAlterazione not in self.alterazioni:
            raise NotaException("L'alterazione deve appartenere a {-2, 1, 0, 1, 2}")
        self.alterazione = intAlterazione
        
        i=0
        while self.note[i] != self.nome:
            i+=1
        self.grado = i
        self.semitono = self.scala[self.nome] + self.alterazione
    
    def __str__(self):
        return self.nome +self.alterazioni[self.alterazione]
    def __repr__(self):
        return self.__str__()
    
    def __add__(self,intervallo):
        if not isinstance(intervallo, Intervallo):
            raise ArgomentiException ("Voglio un intervallo vero")
        nuovoGrado = self.aggiustaGrado(self.grado + intervallo.dg)
        nuovaNota = Nota(self.note[nuovoGrado],0)
        #print(nuovaNota)
        #print(nuovaNota.semitono)
        intervalloGiustoInSemitoni = self.aggiustaSemitono(nuovaNota.semitono - self.semitono)
        #print(nuovoGrado)
        #print(intervalloGiustoInSemitoni)
        nuovaAlterazione = intervallo.ds -intervalloGiustoInSemitoni
        if nuovaAlterazione not in self.alterazioni:
            raise NotaException("Che razza di intervallo è?")
        del(nuovaNota)
        return Nota(self.note[nuovoGrado],nuovaAlterazione)
    
    def __sub__(self,nota):
        if not isinstance(nota, Nota):
            raise ArgomentiException ("Voglio una nota vera")
        distanzaGradi = abs(self.grado - nota.grado)
        
        distanzaSemitoni = self.semitono - nota.semitono
        return Intervallo(distanzaGradi,distanzaSemitoni)
    
    def aggiustaGrado(self,grado):
        while grado < 0:
            grado += len(self.note)
        grado = grado % len(self.note)
        return grado
        
    def aggiustaSemitono(self,semitono):
        while semitono < 0:
            semitono += self.numSemitoni
        semitono = semitono % self.numSemitoni
        return semitono
        
n= Nota("c",0)
i = Intervallo(6,8)
n+i
