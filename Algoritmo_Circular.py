def circular(processos, quantum, trocaContexto):
    turn_around = [0] * len(processos)  

    tempo_atual = 0  
    while True:
        if sum(processos) <= 0:
            print("Todos os processos foram executados!")
            break
        else:
            for i in range(len(processos)):
                if processos[i] <= 0:

                    print(f"\nP{i} já Finalizado")

                elif processos[i] <= quantum:
                    tempo_atual += processos[i]
                    processos[i] -= processos[i]

                    print(f"\nP{i} executa")
                    print(f"Termino em T-{tempo_atual}")

                    if processos[i] == 0:
                        turn_around[i] = tempo_atual
                        print(f"Processo P{i} terminou em T-{tempo_atual}")
                        print("TROCA DE CONTEXTO")
                        tempo_atual += trocaContexto

                else:
                    tempo_atual += quantum
                    processos[i] -= quantum

                    print(f"\nP{i} executa")
                    print(f"Termino em T-{tempo_atual}")
                    print("TROCA DE CONTEXTO")
                    tempo_atual += trocaContexto
                    turn_around[i] = tempo_atual

            print("-" * 30)

    print(f"tempo onde acabou cada processo: {turn_around}")
    return turn_around


def tempoMedio(lista_de_processos, lista_de_tempos):
    resultado = sum(lista_de_tempos) / (len(lista_de_processos))
    print(f"Tempo Médio de Turnaround = {resultado:.2f}")


def main():
    
    qtdProcessos = int(input('Insira a quantidade de processos: '))

    processos = list()

    for i in range(qtdProcessos):
        processo = int(input(f'Digite o tamanho do processo {i+1}: '))
        processos.append(processo)
    
    print(f'Processos: {processos}')
    quantum = int(input('\nInsira o tamanho do quantum: '))
    trocaContexto = int(input('\nInsira o valor da troca de contexto: '))

    turnAround = circular(processos, quantum, trocaContexto)
    tempoMedio(processos, turnAround)

    
main()
