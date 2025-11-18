class Departamento:
    def _init_(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.professores = []

    @classmethod
    def criar_departamento_exatas(cls, nome):
        return cls(nome, "EXA")

    @classmethod
    def criar_departamento_humanas(cls, nome):
        return cls(nome, "HUM")

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def listar_professores(self):
        return self.professores


# Exemplo de uso
if _name_ == "_main_":
    dept_exatas = Departamento.criar_departamento_exatas("Matemática e Computação")
    dept_humanas = Departamento.criar_departamento_humanas("Letras e Filosofia")

    dept_exatas.adicionar_professor("Prof. João")
    dept_exatas.adicionar_professor("Prof. Maria")

    dept_humanas.adicionar_professor("Prof. Ana")
    
    print(f"Departamento: {dept_exatas.nome} - Sigla: {dept_exatas.sigla}")
    print(f"Professores: {dept_exatas.listar_professores()}")

    print(f"Departamento: {dept_humanas.nome} - Sigla: {dept_humanas.sigla}")
    print(f"Professores: {dept_humanas.listar_professores()}")