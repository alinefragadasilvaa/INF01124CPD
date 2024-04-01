import utils
import sorts
import time

def testeUm(entrada, saida):
    vetores = utils.leEntrada(entrada)

    for vetor in vetores:
        tamanho, vetor = utils.montaVetor(vetor)

        # ordena três vezes usando as três sequências
        for id in range(3):
            # imprime vetor inicial
            linha = ' '.join(list(map(str, vetor.copy())))
            utils.escreveSaida(saida, linha +  ' SEQ=' + sorts.nomeSequencia(id)  + '\n')

            # shell(0), knuth(1) e ciura(2)
            sequencia = sorts.defineSequencia(id)
            indice = sorts.primeiroDeslocamento(sequencia, tamanho)

            # ordena vetor
            print('Ordenando vetor de ' + str(tamanho) + ' elementos usando ' + sorts.nomeSequencia(id) + '...')
            sorts.shellSort(vetor.copy(), tamanho, indice, sequencia, True, saida) # true imprime vetor parcialmente ordenado

def testeDois(entrada, saida):
    vetores = utils.leEntrada(entrada)

    for vetor in vetores:
        tamanho, vetor = utils.montaVetor(vetor)

        # ordena três vezes usando as três sequências
        for id in range(3):
            # shell(0), knuth(1) e ciura(2)
            sequencia = sorts.defineSequencia(id)
            indice = sorts.primeiroDeslocamento(sequencia, tamanho)

            # ordena vetor
            inicio = time.process_time() # em segundos
            print('Ordenando vetor de ' + str(tamanho) + ' elementos usando ' + sorts.nomeSequencia(id) + '...')
            sorts.shellSort(vetor.copy(), tamanho, indice, sequencia, False) # false não imprime vetor parcialmente ordenado
            fim = time.process_time() # em segundos

            # calcula tempo de ordenação em milissegundos
            tempo = utils.converteSegundos(fim-inicio)

            # imprime saida
            utils.escreveSaida(saida, sorts.nomeSequencia(id) + ',' + str(tamanho) + ',' + str(tempo) + ',' + 'Intel® Core™ i5-8265U CPU @ 1.60GHz × 8\n')
            
# teste com exemplo do enunciado
testeUm('Inputs/entrada0.txt', 'Outputs/saida0.txt') 

# primeiro teste
testeUm('Inputs/entrada1.txt', 'Outputs/saida1.txt')

# segundo teste
testeDois('Inputs/entrada2.txt', 'Outputs/saida2.txt')