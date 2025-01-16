'''
Classe Produto e método desconto

Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

1 - Cada produto deve ter um preço e um nome. ✓
2 - A classe deve ter um método construtor e o método dundle str.
3 - A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.

'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self): # Sobescreve uma informação padrão
        return f'Produto: {self.nome} - R$ {self.preco}'
    
    def desconto(self, percentual):
        totalComDesconto = self.preco * percentual / 100
        return print(f'Preco do produto {self.nome} com desconto de {percentual}%: {self.preco - totalComDesconto}') 
    
chocolate = Produto('Galak', 200)
print(chocolate)
chocolate.desconto(10)
print(chocolate)
