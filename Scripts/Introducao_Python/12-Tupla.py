gamesTuple = ('Fifa 23', 'Red Dead 2', 'Start Wars',
              'Mario Odyssey', 'The Legend of Selda')
print(gamesTuple)
print(type(gamesTuple))
# name = ('João')
# print(type(name)) # Não é uma tupla pois só tem 1 item

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Buscar o ultimo item da tupla
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posiçãop
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[2:])

# 5 - Recuperar um item da tupla pelo índice
print(gamesTuple.index('Red Dead 2'))

# - Não possibilita adicionar valores na tupla
# - Não possibilita remover valores na tupla
# - Não possibilita ordenar valores na tupla