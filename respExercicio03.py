# respExercicio03.py

class Professor:
    def _init_(self, nome: str, departamento: str, salario_inicial: float):
        self.nome = nome
        self.departamento = departamento
        self._salario = salario_inicial  # atributo privado

    # Getter para salario (propriedade)
    @property
    def salario(self) -> float:
        return self._salario

    # Setter para salario com checagem de positivdade
    @salario.setter
    def salario(self, novo_salario: float) -> None:
        if novo_salario > 0:
            self._salario = novo_salario
        else:
            print("Erro: Salário deve ser um valor positivo!")