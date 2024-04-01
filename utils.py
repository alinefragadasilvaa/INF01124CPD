# retorna uma lista das linhas do arquivo (strings)
def leEntrada(nome): 
    arq = open(nome, 'r')
    return arq.readlines() 

# recebe uma linha (string) e o nome do arquivo e escreve uma nova linha no fim arquivo
def escreveSaida(nome, linha):
    arq = open(nome, 'a')
    arq.write(linha) 

# recebe uma linha do arquivo (string) e retorna um vetor de inteiros e seu tamanho
def montaVetor(linha):
    vetor = linha.split(' ')
    tamanho = int(vetor[0]) # primeiro elemento é o tamanho do vetor
    return tamanho, list(map(int, vetor[1:tamanho+1])) # retira o \n
    
# recebe valor em segundos e retorna valor em milissegundos
def converteSegundos(segundos):
    return segundos * 1000






