class Filme:
    
    plataforma = 'Netflix'

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
        print(f'Plataforma: {Filme.plataforma}')
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

# Modificando a plataforma
Filme.plataforma = 'HBO Max'
avatar.avaliacao(8.0)
avatar.avaliacao(7.5)
avatar.fichaTecnica()
avatar.media()