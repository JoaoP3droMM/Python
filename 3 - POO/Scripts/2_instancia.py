class Filme:
    name = ''
    anoLancamento = 0
    inclusoNoPlano = False
    nota = 0
    duracaoEmMinutos = 0

# Primeiro Filme #
filme1 = Filme()
filme1.name = 'Venom - A Última Rodada'
filme1.anoLancamento = 2024
filme1.inclusoNoPlano = True
filme1.nota = 5.0
filme1.duracaoEmMinutos = 110
print('## Dados do filme1 ##')
print(f'Nome do filme: {filme1.name} \nAno de Lançamento: {filme1.anoLancamento}')

# Segundo Filme #
filme2 = Filme()
filme2.name = 'Moana 2'
filme2.anoLancamento = 2024
filme2.inclusoNoPlano = True
filme2.nota = 4.0
filme2.duracaoEmMinutos = 100
print('## Dados do Filme ##')
print(f'Nome do filme: {filme2.name} \nAno de Lançamento: {filme2.anoLancamento}')