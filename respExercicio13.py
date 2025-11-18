# respExercicio13.py

class Veiculo:
    def _init_(self):
        self._velocidade = 0
        self._incremento = 20  # Quanto aumenta ou diminui na aceleração/freada
    
    def acelerar(self):
        nova_velocidade = self._velocidade + self._incremento
        self._velocidade = min(nova_velocidade, self._velocidade_maxima)

    def frear(self):
        nova_velocidade = self._velocidade - self._incremento // 2
        self._velocidade = max(nova_velocidade, 0)

    def get_velocidade(self):
        return self._velocidade


class Carro(Veiculo):
    def _init_(self):
        super()._init_()
        self._velocidade_maxima = 180


class Bicicleta(Veiculo):
    def _init_(self):
        super()._init_()
        self._velocidade_maxima = 50


class Aviao(Veiculo):
    def _init_(self):
        super()._init_()
        self._velocidade_maxima = 900


class ControladorTrafego:
    def controlar(self, veiculo):
        veiculo.acelerar()
        veiculo.acelerar()
        veiculo.frear()


# Exemplo de uso para testar:

def testar_veiculo(veiculo):
    print(f"Testando {type(veiculo)._name_}")
    veiculo.acelerar()
    veiculo.acelerar()
    print(f"Velocidade: {veiculo.get_velocidade()} km/h")
    veiculo.frear()
    print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h
")


if _name_ == "_main_":
    carro = Carro()
    bicicleta = Bicicleta()
    aviao = Aviao()

    testar_veiculo(carro)
    testar_veiculo(bicicleta)
    testar_veiculo(aviao)