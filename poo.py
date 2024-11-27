class Pessoas:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

class Aluno(Pessoas):
    def cancelar_matricula(self):
        print(f'A matricula de{self.nome} foi cancelada')

class Professor(Pessoas):
    def receber_aumento(self,aumento):
        print(f'O salário do(a) professor(a){self.nome} foi aumentado')

class Secretária(Pessoas):
    def mudar_trabalho(self,novo_cargo):
        print(f'{self.nome} agora trabalha como{novo_cargo}.')

aluno1 = Aluno('João', 20, 'Masculino') 
aluno1.cancelar_matricula()

professor1 = Professor('Carol', 25, 'Feminino')
professor1.receber_aumento(1000)

secretaria1 = Secretária('Jorge', 50, 'Masculino')
secretaria1.mudar_trabalho('Gestor')

