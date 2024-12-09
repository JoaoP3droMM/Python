class Filme:
    def __init__(self, name, anoLancamento, inclusoNoPlano, nota, duracaoEmMinutos):
        self.name = name
        self.anoLancamento = anoLancamento
        self.inclusoNoPlano = inclusoNoPlano
        self.nota = nota
        self.duracaoEmMinutos = duracaoEmMinutos

    def __str__(self): # Sobescreve uma informação padrão
        return f'Filme: {self.name}'

filme = Filme('Venom - A Última Rodada', 2024, False, 5.0, 110)
filme2 = Filme('Avatar - O Caminho da Água', 2022, False, 4.5, 192)
print(filme.name)
print(filme2.name)
print(filme)