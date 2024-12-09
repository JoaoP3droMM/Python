class Filme:
    def __init__(self, name, anoLancamento, inclusoNoPlano, nota, duracaoEmMinutos):
        self.name = name
        self.anoLancamento = anoLancamento
        self.inclusoNoPlano = inclusoNoPlano
        self.nota = nota
        self.duracaoEmMinutos = duracaoEmMinutos

    def __str__(self): # Sobescreve uma informação padrão
        return f'Filme: {self.name}'
    
    def fichaTecnica(self):
        print('\n## Dados do Filme ##')
        print(f'Nome do filme: {self.name}')
        print(f'Ano de lançamento: {self.anoLancamento}')
        print(f'Está no plano? {self.inclusoNoPlano}')
        print(f'Avaliação do filme: {self.nota}')
        print(f'Duração do filme: {self.duracaoEmMinutos}')

venom2 = Filme('Venom - A Última Rodada', 2024, False, 5.0, 110)
avatar2 = Filme('Avatar - O Caminho da Água', 2022, False, 4.5, 192)
venom2.fichaTecnica()
avatar2.fichaTecnica()