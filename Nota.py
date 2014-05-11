from Exceptions import *
from Intervallo import *
import sys
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
        if intOttava < 0:
            raise Exception("Ottava deve essere positiva")
        self.ottava = intOttava 
    
    def __str__(self):
        return self.nome +self.alterazioni[self.alterazione]+"".join("'" for x in range (self.ottava-2))
    def __repr__(self):
        return self.__str__()
    
    def __add__(self,intervallo):
        print(str(intervallo),file=sys.stderr)
        if not isinstance(intervallo, Intervallo):
            raise ArgomentiException ("Voglio un intervallo vero")
        nuovoGrado = self.aggiustaGrado(self.grado + intervallo.dg)
        ott = self.ottava
        if self.grado + intervallo.dg < 0:
            ott -= 1
        elif self.grado+intervallo.dg > 6:
            ott += 1
        nuovaNota = Nota(self.note[nuovoGrado],0,ott)
        
        intervalloGiustoInSemitoni = (self - nuovaNota).ds
        if self > nuovaNota:
            intervalloGiustoInSemitoni = -intervalloGiustoInSemitoni        
        nuovaAlterazione = intervallo.ds -intervalloGiustoInSemitoni
        if nuovaAlterazione not in self.alterazioni:
            raise NotaException("Che razza di intervallo è (nota: "+str(self)+", ottenuta alterazione "+str(nuovaAlterazione)+")?\n\t"+str(intervallo))
        del(nuovaNota)
        return Nota(self.note[nuovoGrado],nuovaAlterazione,ott)
    
    def __sub__(self,nota):
        if not isinstance(nota, Nota):
            raise ArgomentiException ("Voglio una nota vera, ho ricevuto "+nota.__class__.__name__)
        sotto = nota
        sopra = self
        if sotto > sopra:
            sopra,sotto = sotto,sopra
        
        distanzaGradi = self.aggiustaGrado(sopra.grado - sotto.grado)
        
        distanzaSemitoni = self.aggiustaSemitono(sopra.semitono - sotto.semitono)
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
    
    def __gt__(self,nota):
        gradoA = self.ottava * 12 + self.semitono
        gradoB = nota.ottava * 12 + nota.semitono
        return gradoA > gradoB
    def __le__(self,nota):
        return not nota.__gt__(self)
        
    def __lt__(self,nota):
        gradoA = self.ottava * 12 + self.semitono
        gradoB = nota.ottava * 12 + nota.semitono
        return gradoA < gradoB
    def __ge__(self,nota):
        return not nota.__lt__(self)
n= Nota("c",0,3)
n1 = Nota("g",0,4)
#i = Intervallo(6,8)
#n+i
