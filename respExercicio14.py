from abc import ABC, abstractmethod

# Interfaces menores e específicas
class Trabalhavel(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Alimentavel(ABC):
    @abstractmethod
    def comer(self):
        pass

class Descansavel(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Programavel(ABC):
    @abstractmethod
    def programar(self):
        pass

# Classes concretas implementando apenas as interfaces necessárias
class Desenvolvedor(Trabalhavel, Alimentavel, Descansavel, Programavel):
    def _init_(self, nome):
        self.nome = nome
    
    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")
    
    def comer(self):
        print(f"{self.nome} está comendo.")
    
    def dormir(self):
        print(f"{self.nome} está dormindo.")
    
    def programar(self):
        print(f"{self.nome} está programando.")

class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def _init_(self, nome):
        self.nome = nome
    
    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")
    
    def comer(self):
        print(f"{self.nome} está comendo.")
    
    def dormir(self):
        print(f"{self.nome} está dormindo.")

class Robo(Trabalhavel, Programavel):
    def _init_(self, nome):
        self.nome = nome
    
    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")
    
    def programar(self):
        print(f"{self.nome} está programando.")

# Exemplo de uso:
if _name_ == "_main_":
    desenvolvedor = Desenvolvedor("Ana")
    gerente = Gerente("Carlos")
    robo = Robo("R2D2")

    # Desenvolvedor faz tudo
    desenvolvedor.trabalhar()
    desenvolvedor.comer()
    desenvolvedor.programar()
    desenvolvedor.dormir()

    # Gerente não programa
    gerente.trabalhar()
    gerente.comer()
    gerente.dormir()

    # Robô não come nem dorme
    robo.trabalhar()
    robo.programar()