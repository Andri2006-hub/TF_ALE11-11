# Resposta_10.py

class Pessoa:  # Erro 1 corrigido: nome da classe com letra maiúscula
    def _init_(self, nome, idade):
        self.nome = nome  # Erro 2 corrigido: atribuír ao atributo de instância
        self.idade = idade
        self.__cpf = None  # Encapsulamento mantido, sem erro
    
    def apresentar(self):  # Erro 4 corrigido: método precisa de 'self' como parâmetro
        return f"Olá, sou {self.nome}"

class Estudante(Pessoa):
    def _init_(self, nome, idade, curso):
        super()._init_(nome, idade)  # Erro 5 corrigido: chamar super() para inicializar atributos da superclasse
        self.curso = curso
        self.notas = []
    
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
    
    def calcular_media(self):
        if len(self.notas) == 0:  # Erro 7 corrigido: evitar divisão por zero
            return 0
        return sum(self.notas) / len(self.notas)  # Cálculo correto

class Professor(Pessoa):
    def _init_(self, nome, idade, departamento, salario):
        super()._init_(nome, idade)
        self.departamento = departamento
        self.salario = salario
    
    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"

# Testando o código
estudante = Estudante("João", 20, "Engenharia")
professor = Professor("Dr. Silva", 45,