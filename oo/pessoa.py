class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    gabriel = Pessoa(nome='Gabriel')
    lucia = Pessoa(gabriel, nome='Lucia')
    print(Pessoa.cumprimentar(lucia))
    print(id(lucia))
    print(lucia.cumprimentar())
    print(lucia.nome)
    print(lucia.idade)
    for filho in lucia.filhos:
        print(filho.nome)
