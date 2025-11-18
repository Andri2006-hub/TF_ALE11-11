# respExercicio12.py
from abc import ABC, abstractmethod

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass
    
class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.90  # 10% de desconto

class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.85  # 15% de desconto

class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.80  # 20% de desconto

class ProcessadorPagamento:
    def processar(self, valor, calculador_desconto: CalculadorDesconto):
        return calculador_desconto.calcular(valor)

# Demonstração da extensão sem modificar código existente
class DescontoBlackFriday(CalculadorDesconto):
    def calcular(self, valor):
        return valor * 0.70  # 30% de desconto

if _name_ == "_main_":
    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    desconto_estudante = DescontoEstudante()
    desconto_funcionario = DescontoFuncionario()
    desconto_vip = DescontoVIP()
    desconto_black_friday = DescontoBlackFriday()  # novo desconto sem alterar classes anteriores

    print(f"Estudante: R$ {pagamento.processar(valor_original, desconto_estudante)}")
    print(f"Funcionário: R$ {pagamento.processar(valor_original, desconto_funcionario)}")
    print(f"VIP: R$ {pagamento.processar(valor_original, desconto_vip)}")
    print(f"Black Friday: R$ {pagamento.processar(valor_original, desconto_black_friday)}")