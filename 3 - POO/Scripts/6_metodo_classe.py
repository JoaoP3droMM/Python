'''
1 - O método de classe utiliza o parâmetro referente a classe.

2 - O método de classe pode acessar ou modificar o estado da classe.

3 - Usamos o decorator @classmethod para criar um método de classe
'''

class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall(r'é (\w+) e o preço é (\d+)', string)
        name = item[0][0]
        price = item[0][1]
        return cls(name, int(price))

    def __str__(self):
        return f'Console: {self.name}, Preço: {self.price} reais'

wiiU = Console.from_text('Meu console é WiiU e o preço é 1000 reais')
xboxOne = Console.from_text('Meu console é XboxOne e o preço é 2000 reais')

print(wiiU)