dic = {'Gandalf': ('Fisica',    0.76,16.65),'Arun':    ('Fisica',    0.68,23.24),'Anil':    ('Fisica',    0.43,25.90),
     'Masvidal':('Matematica',0.38,22.00),'Case':    ('Matematica',0.76,32.00),'Mercedes':('Matematica',0.52,25.90),
     'Mario':   ('Portugues', 0.63,22.35),'Maria':   ('Portugues', 0.76,28.00),'Eugenio': ('Portugues', 0.96,42.00),
     'Andre':   ('Biologia',  0.58,20.00),'Francois':('Biologia',  0.55,16.65),'Joe':     ('Biologia',  0.65,26.00),
}
mat = 'Biologia'
scd = 0.9
sel = []
cha = []
aux = dic.items()
for i in aux:
    (a,b) = i
    (x,y,z) = b
    if x == mat and y >= scd:
        sel.append(a)
        cha.append(z)
if cha != []:
    menor = min(cha)
    aux2 = cha.index(menor)
    prof = sel[aux2]
else:
    prof = 'Nenhum candidato'
print(sel)
print(cha)
print(prof)
