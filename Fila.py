class Fila:
    def __init__(self, tamanho) -> None:
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0

    def enfileirar(self, cidade):
        if not Fila.filaCheia(self):
            if self.fim == self.tamanho - 1:
                self.fim = -1

            self.fim += 1
            self.cidades[self.fim] = cidade
            self.numeroElementos += 1
        else:
            print('A fila ja esta cheia')

    def desenfileirar(self):
        if not Fila.filaVazia(self):
            temp = self.cidades[self.inicio]
            self.inicio += 1
            if self.inicio == self.tamanho:
                self.inicio = 0

            self.numeroElementos -= 1
            return temp
        else:
            print('A fila ja esta vazia')
            return None
        
    def getPrimeiro(self):
        return self.cidades[self.inicio]
    
    def filaVazia(self):
        return self.numeroElementos == 0
    
    def filaCheia(self):
        return self.numeroElementos == self.tamanho
    
from Mapa import Mapa
mapa = Mapa()

fila = Fila(5)

print(f'Enfileirando...')
fila.enfileirar(mapa.canoinhas)
fila.enfileirar(mapa.irati)
fila.enfileirar(mapa.balsaNova)
print(fila.getPrimeiro().nome)

print('Desenfilerando...')
fila.desenfileirar()
print(fila.getPrimeiro().nome)