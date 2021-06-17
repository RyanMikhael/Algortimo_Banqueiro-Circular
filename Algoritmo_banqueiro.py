import numpy as np

#Iniciando o programa
Titulo = "Algoritmo do banqueiro"
print(Titulo.center(140).upper()+ '\n')
qtd = int(input('Insira a quantidade de recursos existentes do vetor: '))
qtd_processos = int(input('Insira a quantidade de processos: '))


# Vetor de recursos existentes E
def RecursosTotais(qtd):
    E = list()
    for i in range(qtd):
        recurso = int(input(f'Insira a quantidade do recurso {i+1}: '))
        E.append(recurso)
    
    return E


# Vetor de recursos disponíveis A
def RecursosDisponiveis(qtd):
    A = list()
    for i in range(qtd):
        recurso = int(input(f'Insira a quantidade do recurso {i+1} disponível: '))
        A.append(recurso)
    
    return A


# Pede a inserção da matriz de alocação C
def MatrizAlocaçao(qtd_processos, qtd):
    matriz = list()
    for i in range(qtd_processos):
        processos = list()
        for j in range(qtd):
            recurso = int(input(f'Insira a quantidade do recurso {j+1} disponível para o processo {i+1}: '))
            processos.append(recurso)

        matriz.append(processos)
    return matriz


# Pede a inserção da matriz de requisições R
def MatrizRequisiçoes(qtd_processos, qtd):
    matriz_requisiçoes = list()
    for i in range(qtd_processos):
        processos = list()
        for j in range(qtd):
            recurso = int(input(f'Insira a quantidade do recurso {j+1} que é necessário para o processo {i+1}: '))
            processos.append(recurso)

        matriz_requisiçoes.append(processos)
    return matriz_requisiçoes


#verifica se a matriz de alocação está correta
def verificaçaoMatriz(matriz, E, A):
    soma = np.array([0, 0, 0])
    for i in range(len(matriz)):
        soma += matriz[i]
    
    x = np.array(E)
    y = np.array(A)
    z = x - y
    
    for c in range(len(soma)):
        if soma[c] == z[c]:
            continue
        else:
            return False
    return True


# Verificar se há ou não deadlock
def banqueiro(qtd_processos, qtd, recursosDisponiveis, requisiçoes,matriz ):

    run = np.ones(qtd_processos)
    recursosDisponiveis = np.array(recursosDisponiveis)
    requisiçoes = np.array(requisiçoes)
    matriz = np.array(matriz)


    while np.count_nonzero(run) > 0:
        alocou = False
        for n in range(qtd_processos):

            if run[n] != 0:
                if all(i >= 0 for i in recursosDisponiveis - (requisiçoes[n] - matriz[n])):
                    alocou = True
                    print(f'P{n+1} está rodando!')
                    input('Pressione <Enter> para prosseguir \n')
                    run[n] = 0
                    recursosDisponiveis += matriz[n]
                    matriz[n] = np.zeros(qtd)
                    print(f'\nvetor de recursos disponíveis A >>> {recursosDisponiveis}')
                    print('\nMatriz de requisições R: \n')
                    for i in range(len(matriz)):
                        print(f'P{i+1} -- {requisiçoes[i]}')

        if alocou == False:
            print('Os processos entrarão em deadlock!')
            exit()
        
        print('Os processos não entrarão em deadlock')
                    
    


# Imprimir os resultados
def main():
    
    #Instanciando as funções
    recursosTotais = RecursosTotais(qtd)
    recursosDisponiveis = RecursosDisponiveis(qtd)
    matriz = MatrizAlocaçao(qtd_processos, qtd)
    verificacao = verificaçaoMatriz(matriz, recursosTotais, recursosDisponiveis)
    requisiçoes = MatrizRequisiçoes(qtd_processos, qtd)
    

    if verificacao == True:
        print(f'\nvetor de recursos existentes E >>> {recursosTotais}')
        print(f'\nvetor de recursos disponíveis A >>> {recursosDisponiveis}')

        print('\nMatriz de alocação C:\n')
        for c in range(len(matriz)):
            print(f'P{c+1} -- {matriz[c]}')

        print('\nMatriz de requisições R: \n')
        for i in range(len(matriz)):
            print(f'P{i+1} -- {requisiçoes[i]}')

        banqueiro(qtd_processos, qtd, recursosDisponiveis, requisiçoes, matriz)

    else:
        print('Os valores inseridos para a matriz de alocação C estão incorretos!')
    

main()
