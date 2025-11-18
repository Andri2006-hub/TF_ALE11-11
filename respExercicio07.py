# respExercicio07.py

class Aluno:
    def _init_(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas_inscritas = []

    def listar_disciplinas(self):
        if not self.disciplinas_inscritas:
            print(f"{self.nome} não está inscrito em nenhuma disciplina.")
        else:
            print(f"Disciplinas inscritas por {self.nome}:")
            for disciplina in self.disciplinas_inscritas:
                print(f"- {disciplina.nome} ({disciplina.codigo})")


class Disciplina:
    def _init_(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.alunos_matriculados = []

    def listar_alunos(self):
        if not self.alunos_matriculados:
            print(f"Nenhum aluno matriculado na disciplina {self.nome}.")
        else:
            print(f"Alunos matriculados em {self.nome}:")
            for aluno in self.alunos_matriculados:
                print(f"- {aluno.nome} ({aluno.matricula})")


class Secretaria:
    @staticmethod
    def inscrever_aluno(aluno, disciplina):
        # Adiciona aluno na lista da disciplina se ainda não estiver
        if aluno not in disciplina.alunos_matriculados:
            disciplina.alunos_matriculados.append(aluno)
        # Adiciona disciplina na lista do aluno se ainda não estiver
        if disciplina not in aluno.disciplinas_inscritas:
            aluno.disciplinas_inscritas.append(disciplina)


# Exemplo de uso (podem ser removidos antes da entrega)
if _name_ == "_main_":
    aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
    aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")
    disciplina1 = Disciplina("POO", "POO001", 60)
    disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

    Secretaria.inscrever_aluno(aluno1, disciplina1)
    Secretaria.inscrever_aluno(aluno1, disciplina2)
    Secretaria.inscrever_aluno(aluno2, disciplina1)

    aluno1.listar_disciplinas()
    print()
    disciplina1.listar_alunos()