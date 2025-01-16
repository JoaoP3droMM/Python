'''
Avaliação e Média da Nota de Filmes

Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

1 - Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota com parâmetro e que essa nota seja salva no atributo específico da classe.
2 - Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim.
3 - Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.

'''


class Filme:
    def __init__(self, name, anoLancamento, inclusoNoPlano, duracaoEmMinutos):
        self.name = name
        self.anoLancamento = anoLancamento
        self.inclusoNoPlano = inclusoNoPlano
        self.totalAvaliacoes = 0
        self.duracaoEmMinutos = duracaoEmMinutos
        self.avaliadores = 0

    def __str__(self): # Sobescreve uma informação padrão
        return f'Filme: {self.name}'
    
    def fichaTecnica(self):
        print('\n## Dados do Filme ##')
        print(f'Nome do filme: {self.name}')
        print(f'Ano de lançamento: {self.anoLancamento}')
        print(f'Está no plano? {self.inclusoNoPlano}')
        print(f'Avaliação do filme: {self.totalAvaliacoes}')
        print(f'Duração do filme: {self.duracaoEmMinutos}')
        print(f'Total avaliadores: {self.avaliadores}')

    def avaliacao(self, nota):
        self.totalAvaliacoes += nota # totalAvaliacoes = totalAvaliacoes + nota
        self.avaliadores += 1

    def media(self):
        print(f'Média do filme {self.name}: {self.totalAvaliacoes / self.avaliadores}')

mario = Filme('Super Mário Bros', 2023, False, 135)
avatar = Filme('Avatar', 2023, False, 180)

mario.avaliacao(9.5)
mario.avaliacao(10.0)
mario.fichaTecnica()
mario.media()