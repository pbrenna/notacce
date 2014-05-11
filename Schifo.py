from Nota import *
from Exceptions import *
from Intervallo import *
from copy import deepcopy
import random
class Accordo:
    def __init__(self, *Note):
        self.note = Note
    @property
    def consonante(self):
        punteggio = 0
        intX = 0
        for x in self.note:
            if x is not None:
                for y in range(intX+1,len(self.note)):
                    if self.note[y] is not None:
                        punteggio += (x - self.note[y]).consonante
            intX += 1
        return punteggio
    @property
    def boolConsonante(self):
        return self.consonante > self.nVoci
    @property
    def nVoci(self):
        i = 0
        for x in self.note:
            i += 1 if x is not None else 0
        return i
    def __repr__(self):
        return repr(self.note) + ", consonante: "+ str(self.consonante)

n1 = Nota("g",0,3)
n2 = Nota("e",0,4)
n3 = Nota("c",0,4)
acc = Accordo(n3,n2,n1,n)
def concatenaAccordo(accPrecedente,accSuccessivo):
    for x in range(accPrecedente.nVoci):
        if accSuccessivo.note[x] is not None:
            interv = accPrecedente.note[x] - accSuccessivo.note[x]
            if interv.consonante < 0 and interv.ds != 1:
                return False
    return True

def nuovoAccordo (accPrecedente,tentativiEsterni = 0):
    if tentativiEsterni > 15: 
        raise Exception("non riesco a concatenare un tubo!")
    muoviVoce = random.choice(range(accPrecedente.nVoci))
    #una voce la muoviamo per grado
    nuoveNote = [None] * accPrecedente.nVoci
    while True:
        muoviDi = random.choice([(-1,-2),(-1,-1),(1,1),(1,2)])
        try: 
            nuoveNote[muoviVoce] = accPrecedente.note[muoviVoce] + Intervallo(*muoviDi)
            break
        except NotaException:
            continue
        
    movimenti = [unisonoG, semitono, secondam, secondaM, terzam, terzaM, quartaG,quintaG]
    intVoce = 0
    tentativi = 0
    while not Accordo(*nuoveNote).boolConsonante:
        for nota in nuoveNote:
            if nota is None:
                random.shuffle(movimenti)
                movimenti = movimenti[::-1]
                for mov in movimenti:
                    m = (-mov[0],-mov[1])
                    if random.choice([0,1]) == 0:
                        m = mov
                        
                    try: 
                        nuoveNote[intVoce] = accPrecedente.note[intVoce] + Intervallo(*m)
                    except NotaException:
                        continue
                    if concatenaAccordo(accPrecedente, Accordo(*nuoveNote)):
                        break
            intVoce += 1
        tentativi += 1
        if tentativi > 40:
            break
    if tentativi > 20:
        return nuovoAccordo(accPrecedente,tentativiEsterni+1)
    return Accordo (*nuoveNote)
    
lista = [acc]
for accN in range(8):
    lista.append(nuovoAccordo(lista[accN]))

def lilypondize(lista):
    conta = lista[0].nVoci
    voci = []
    for x in range(conta):
        s = ""
        for y in lista:
            s+= str(y.note[x]) + " "
        voci.append(s)
    ret = "\\version \"2.18.2\"\n\
\score {\n\
    \\new PianoStaff<< \n\
        \\new Staff <<\\new Voice {"+voci[0] +"}\\\\ \n\
        \\new Voice {"+voci[1] +"}>>\\\\ \n\
        \\new Staff <<\n\
        \\new Voice {"+voci[2] +"} \\\\ \n\
        \\new Voice {"+voci[3] +"}\n\
        >> \n\
    >> \n\
    \layout{}\n\
    \midi{}\n\
}"
    return ret
print (lilypondize(lista))
