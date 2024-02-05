def fai_la_pasta(tipo_pasta,metti_sugo):
    print("metti l'acqua")
    print("metti il sale")
    print("fai bollire")
    print("metti "+tipo_pasta)
    if (metti_sugo):
        print("prepare il sugo")
    print("--------------------------")        



class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("Ciao, sono "+self.nome)

import miomodulo as em
# from miomodulo import persona1 (per importare solo una partecl)

import camelcase
import math
import datetime
import json
import os




class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia  
        
    def saluta(self):
        print("Buongiorno, sono "+self.nome+" "+self.cognome)


    def dai_voto(self):
        print("Bravo, un bell'8")



# per commentare si usa il cancelletto o hashtag

#dfdfsdfsd
#sdfsdfsd


#  messaggio = input("Inserisci il testo del messaggio:")
messaggio = "Test messaggio fisso"

print(messaggio)    

if 50 < 40:
    print ("10 è minore di 40")
print ("fuori if")


x = 5
Y = 6

#Nomi variabili illegali
# - utilizzo di trattini         Esempio: peso-persona
# - se inizia con un numero      Esempio: 12pesoPersona
# - se ci sono degli spazi       Esempio: peso persona

x=y=z= 845

print(x)
print(y)
print(z)


x,y,z = 34,45,65

print(x)
print(y)
print(z)

Totale = x + y + z
print ("Totale=",Totale) 


citta = ["Milano", "Roma", "Firenze","Napoli"]

c1,c2,c3,c4=citta

print(c1)
print(c2)
print(c3)
print(c4)


# str:   x="ciao"
# int:   x=20
# float: x=454.234
# bool:  x=True

#Collezioni di dati
# list:  x = ["Milano", "Roma", "Firenze"]
# tuple: x = ("Milano", "Roma", "Firenze")
# range  x = range(6)
# dict   x = {"nome":"Luca", "eta": 24 }
# set    x = {"Milano","Roma", "Firenze"}

X = 34
print(type(X))

X = 34.454
print(type(X))

X = "Prova stringa"
print(type(X))


x= 54
y= "34"

#print (y+x)

x="Ciao"
y=" sono Marco"

print(x+y)

x="Ciao sono "
y=4
print (x+str(y))



x= 3434
y= "134"
print (x+int(y))


x= float(5)

print (x)


x="""
Questo è un esempio di stringa 
sviluppata su più righe. Si può ottenere
utilizzando tripli doppi apici opure tripli singolo apice

-----
"""
print (x)


x="prova"

print(x[1])
print(len(x))
print ("----------")

for carattere in "prova":
    print (carattere)



print ("--------------")

x="  Prova di stringa lunga   lunga"
print (x[5:8])

print(x.upper())
print(x.strip())

print(x.replace("o","W"))

prova = "Ciao, sono Marco e sono nato il {}, peso {} Kg e sono alto {} cm"

print (prova.format("14 ottobre 1964",64,174))

prova ="Ciao sono Roberto e sono \"figo\""
print (prova)

prova ='Sono alla ricerca dell\'amore'
print (prova)


x=50
y=30

if  (x<y):
    print (x,"è minore di",y)
else:
    print (x,"è maggiore di",y)


liste_cose_da_comprare=["pane"]

if liste_cose_da_comprare:
    print ("Devo andare al supermercato")
else:
    print ("Non devo andare al supermercato")    




lista_citta=["Milano", "Roma", "Firenze", "Napoli"]



i=0
while (i<6):
    i +=1
    if (i==4):
        print ("Sono arrivato a 4 e mi mancano 2")
    else:
        print(i)

print("Ciao")

for citta in lista_citta:
    print (citta)

print ("Inizio for in range")

for i in range(9):
    print (i)

print ("Fine for in range")

# Liste: ordinate e modificabile. Permette duplicati
# Tuple: ordinate ma immutabile. Permette duplicati

# Set: non ordinate e non indicizzate. Univoci
# Dictionary: ordinate e modificabile. Univoci


#Esempio Lista

lista1=["Roberta","Giada","Isabella",False, 2323.34]
lista2=["Cabrihna","Best","Slingshot","North"]

print ("tipo di variabile lista1: "+str(type(lista1)))
print ("lunghezza variabile lista1: "+str(len(lista1)))

lista3=list(("Roberta","Giada","Isabella"))

print ("Esempio lista3 ottenuta da una list")
print(lista3[2])


lista3[0]="Giulia"

print(lista3)

lista3[1:3] = ["Carla","Tiziana"]

print(lista3)

lista3.append("Santina")

print(lista3)

lista3.insert(1,"Felicia")

print(lista3)

print ("lista3.extend(lista2)")
lista3.extend(lista2)

print(lista3)

lista3.sort(reverse=True)

print(lista3)


lista4=lista3
lista5=lista3.copy()

lista3[0]="Primo elemento"
print(lista4)
print(lista5)

# Tupla
x=("Milano","Roma")

y=(("Milano","Roma","Berlino","Madrid"))
print(y)

print (type(x))

z=list(y)
z[0]="London"

y=tuple(z)

print(y)


#spacchettare una tupla
(a,b,c,d) = y
print(a)
print(b)
print(c)
print(d)

(a,b,*c) = y
print(a)
print(b)
print(c)
print("..................")

for citta in y:
    print(citta)

print("..................")

for i in range(len(y)):
    print (y[i])

print("..................")

i=0
while i<len(y):
    print (y[i])
    i +=1


tupla1=("trapano","cacciavite", "pinza","chiave inglese","tronchese")
tupla2=("bullone","vite","rondella","colla","nastro")

tuplat=tupla1 + tupla2

print(tuplat)


#Set
x={"Napoli","Milano","Roma","London"}
y={"Milano",False,12.3 }


print(type(x))
print(len(x))

z=set(("Fiat","BMW","Audi","Renault"))

print(x)


for macchina in z:
    print(macchina)

print("Milano" in x)    

z.add("Mercedes Benz")

print(z)

z.update(x)

print (z)

z.remove("Audi")
z.discard("Renault")
print (z)


# Dict

persona = {
    "nome": "Marco",
    "cognome": "Chirico",
    "eta": 44
}

print (persona)
print (type(persona))
print (len(persona))


print (persona["nome"])
print (persona.get("nome"))
print (persona.keys())


fai_la_pasta("i fusilli",False)
fai_la_pasta("gli spaghetti",True)


persona1 = Persona("Luca","Rossi")
persona2 = Persona("Roberta","Cervone")
print(persona1.nome)
print(persona2.nome)

persona1.nome = "Antonio"

persona1.saluta()
persona2.saluta()

del persona1
del persona2

insegnante1 = Insegnante("Dario","Sorrentini","Matematica")
insegnante1.saluta()
print(insegnante1.materia)

insegnante1.dai_voto()

x = em.persona1["nome"]
em.saluta(x)

print(dir(math))

x=datetime.datetime.now()
print(x)

y=datetime.datetime(2020,10,14)
print(y)

print(x.strftime("%B")) 
print(x.strftime("%d/%m/%Y")) 

print(math.log10(50))
print(pow(10,1.7))

# Esempio da Json a Python
x = '{"nome": "Massimo", "cognome": "Gallicano", "eta": 53}'

y = json.loads(x)

print(y)

print(type(y))

# Esempio da Python a Json

x = {"nome": "Massimo",
     "cognome": "Gallicano",
     "eta": 53,
     "isOnline": False,
     "interessi": ["Kite Surf","Running","Skate board","Musica","Film"],
     "librettoRisparmio": 35650.00,
     "fidanzata": None
}

y=json.dumps(x, indent=5)
print(y)

print(type(y))

# Esempio di list

y = json.dumps(["Roma","Milano","Firenze"])
print(y)

x = camelcase.CamelCase()
frase = "ciao stamattina mi sono svegliato tardi"
frase = "ciao stamattina mi sono svegliato tardi"

print(x.hump(frase))

try:
    print(x)
except:
    print("C'è stato un problema")    

print (persona)
operazioni = ("aggiungere","modificare","eliminare")

def start():
    operazione=input("Cosa vuoi fare? ")
    if operazione == operazioni[0]:
        x = input("Aggiungi chiave:valore separati da una virgola: ")
        aggiungi(x.split(","))
    elif operazione == operazioni[1]:
        pass
    elif operazione == operazioni[2]:
        pass

def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave]=valore
    print(persona)


#while True:
#    start()

peso = 64.3
altezza = 172

frase = "Sono Marco, peso {} Kg e sono alto {} cm"

print(frase.format(peso,altezza))

frase = "Sono Marco, peso {p1} Kg e sono alto {p2} cm"

print(frase.format(p1=peso,p2=altezza))

#esempio di lettura file
f = open("testo.txt","r")
#print (f.read())
for riga in f:
    print (riga)

f.close()

#esempio di scrittura file
f = open("testo.txt","w")
f.write("Questa e' la prima riga di file che aggiungo")
f.close()


if os.path.exists("prova.txt"):
    os.remove("prova.txt")
else:
    print("Non esiste il file con questo nome")    

a=856858
print(a >> 2)

for i in range(10):
    pass

print (1+-2)


a='ant'
b="bat"
c='camel'
print(a,b,c,sep='.')

i=5
while i>0:
    i=i //2
    if i % 2 ==0:
        break
else:
    i+=1
print(i)    
        

print (i)
print ("------")


b=range(1, 3)
#b=range(2)
for i in b:
    print("*",end="")
else:
     print("*")   

print ("------")
a=[1,55]     
b=a
b[0]=45
print (a)

print(b)

a= 34
b=a
a=33
print (a, b)

print("-------------")

a=[0]
b=a [:]
a[0]=1

print(a,b)

str = '1234567'
print(str[1:-2])
print(str[1:2])


lst=["a","b","c","d","3e3"]
print(lst)

lst=lst[-3:3]
print(lst)

lst=lst[-1]
print(lst)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


