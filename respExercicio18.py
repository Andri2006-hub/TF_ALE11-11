# respExercicio18.py

class Amplificador:
    def ligar(self):
        print("Ligando amplificador")

    def definir_volume(self, volume):
        print(f"Definindo volume para {volume}")

class DVDPlayer:
    def ligar(self):
        print("Ligando DVD player")

    def reproduzir(self, filme):
        print(f"Reproduzindo {filme}")

class Projetor:
    def ligar(self):
        print("Ligando projetor")

    def modo_widescreen(self):
        print("Projetor em modo widescreen")

class Luzes:
    def diminuir(self, nivel):
        print(f"Diminuindo luzes para {nivel}%")

class PipocaPopper:
    def ligar(self):
        print("Ligando pipoqueira")

    def fazer_pipoca(self):
        print("Fazendo pipoca")

class HomeTheaterFacade:
    def _init_(self):
        self.amplificador = Amplificador()
        self.dvd = DVDPlayer()
        self.projetor = Projetor()
        self.luzes = Luzes()
        self.pipoca = PipocaPopper()

    def assistir_filme(self, filme):
        print(f"Preparando para assistir {filme}...")
        self.amplificador.ligar()
        self.amplificador.definir_volume(5)
        self.dvd.ligar()
        self.projetor.ligar()
        self.projetor.modo_widescreen()
        self.luzes.diminuir(10)
        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()
        self.dvd.reproduzir(filme)

    def fim_filme(self):
        print("Filme finalizado!")
        # Aqui pode-se desligar componentes se desejar
        # Para simplicidade, só imprimimos a mensagem


# Demonstração do uso
if _name_ == "_main_":
    print("# Uso complexo (sem facade)")
    amplificador = Amplificador()
    dvd = DVDPlayer()
    projetor = Projetor()
    luzes = Luzes()
    pipoca = PipocaPopper()

    amplificador.ligar()
    amplificador.definir_volume(5)
    dvd.ligar()
    projetor.ligar()
    projetor.modo_widescreen()
    luzes.diminuir(10)
    pipoca.ligar()
    pipoca.fazer_pipoca()
    dvd.reproduzir("Matrix")

    print("
# Uso simples (com facade)")
    home_theater = HomeTheaterFacade()
    home_theater.assistir_filme("Matrix")
    home_theater.fim_filme()