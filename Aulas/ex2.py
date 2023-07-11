from ex1 import Pessoa


class Pcd(Pessoa):
    def __init__(self, nome, idade, altura, peso, defic):
        super().__init__(nome,  idade, altura, peso)
        self.deficiencia = defic

    def mostrar(self):
        print(f'Nome:{self.nome}\nIdade:{self.idade}\nAltura:{self.altura}\nPeso:{self.peso}\nDeficiencia:{self.deficiencia}\n')


p1 = Pessoa('Limeira', 34, 1.8, 80)
pcd1 = Pcd('João', 22, 1.8, 78, 'Paraplegico')
p1.mostrar()
pcd1.mostrar()

"""
Função especifica da classe filha vai funcionar só na classe filha.
Atributo especifico da classe filha só vai ter na classe filha.
Se a filha mudar uma função da mãe, a versão modificada vai ter prioridade.
Herança serve para voce não ter que escrever tudo de novo para modificar um codigo.
"""
