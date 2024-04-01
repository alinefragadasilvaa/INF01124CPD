import utils

# insertion sort
def insertionSort(vetor, tamanho, deslocamento, inicio):
    for i in range(inicio+deslocamento, tamanho, deslocamento):
        chave = vetor[i]
        j = i-deslocamento
        while j>=0 and vetor[j]>chave:
            vetor[j+deslocamento] = vetor[j]
            j = j-deslocamento
        vetor[j+deslocamento] = chave
    return vetor

# shell sort 
def shellSort(vetor, tamanho, indice, sequencia, acompanhar, saida = None):
    while indice >= 0:
        for inicio in range(sequencia[indice]):
            vetor = insertionSort(vetor, tamanho, sequencia[indice], inicio)
        
        # imprime vetor ordenado parcialmente
        if(acompanhar):
            linha = ' '.join(list(map(str, vetor)))
            utils.escreveSaida(saida, linha + ' INCR=' + str(sequencia[indice]) + '\n')

        indice=indice-1
    return vetor

# contantes para as sequências do shell sort
shell = 0
knuth = 1
ciura = 2

# retorna a sequência escolhida para deslocamento do shell sort
def defineSequencia(id):
    if(id==shell):
        return [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
    if(id==knuth):
        return [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
    if(id==ciura):
        return [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]

# recebe a constante da sequência e retorna seu nome 
def nomeSequencia(id):
    if(id==shell):
        return 'SHELL'
    if(id==knuth):
        return 'KNUTH'
    if(id==ciura):
        return 'CIURA'

# retorna o índice da sequência do primeiro deslocamento do shell sort
def primeiroDeslocamento(sequencia,tamanho):
    i = 0
    for deslocamento in sequencia:
        if deslocamento >= tamanho:
            return i-1
        i=i+1