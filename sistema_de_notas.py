aluno = 0
nota = 0
n_a = []
gab = ['a','b','c','d','e','e','d','c','b','a']
sis = int(input('Para iniciar o sistema de notas aperte a tecla 1: '))
while sis == 1:
    n = []
    nota = 0
    aluno = aluno + 1
    for i in range(0,10,1):
        q = str(input('Entre com as suas respostas da prova: '))
        n.append(q)
    for i in range(0,10,1):
        if n[i] == gab[i]:
            nota = nota + 1
    print('Nota: ',nota)
    n_a.append(nota)
    sis = int(input('Para continuar no sistema de notas aperte 1: '))
print('Maior Nota: ',max(n_a))
print('Menor Nota: ',min(n_a))
print('Total de Alunos que utilizaram o sistema: ',aluno)
print('Media das notas: ',sum(n_a)/len(n_a))
    
                                         
    
