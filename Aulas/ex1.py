class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def mostrar(self):
        print(f'Nome:{self.nome}\nIdade:{self.idade}\nAltura:{self.altura}\nPeso:{self.peso}\n')


# props e aperta enter nesse krl
"""
    @property
    def nome(self):
        return 
    
    @nome.setter
    def nome(self, value):
        pass
"""
