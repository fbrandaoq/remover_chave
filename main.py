pessoa = {
    'Nome':'Fábio Brandão',
    'Idade':'44',
    'Profissão':'Analista',
    'Empresa':'SENAI',
    'Gênero':'Masculino',
    'Cidade':'Samambaia',
}

# remover chave
del pessoa[input('Informe o nome da chave a ser deletada: ')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')