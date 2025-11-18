#respExercicio 01
class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

        class Disciplina:
        def _ _init_ _(self,nome,codigo,carga horaria):
            self.nome = nome
            self.codigo = codigo
            self.carga_horaria = carga_horaria
            #Instanciando objetos Aluno
        aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
        aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")

        #Instanciando objetos Disciplina
        disciplina1 = Disciplina("Programação Orientada a Objetos", "POO001", "60h")
        disciplina2 = Disciplina("Banco de Dados", "BD001", "80h") 

        #imprimindo os atribuitos
        print("Aluno 1.  Nome:")
        print("Matrícula:", aluno1.matricula)
        print("Curso:", aluno1.curso)
        print("Disciplina:", disciplina1.nome)
        print("Código:", disciplina1.codigo)
        print("Carga Horária:", disciplina1.carga_horaria)
        
        print("Aluno 2. Nome:")
        print("Matrícula:", aluno2.matricula)
        print("Curso:", aluno2.curso)
        print("Disciplina:", disciplina2.nome)
        print("Código:", disciplina2.codigo)
        print("Carga Horária:", disciplina2.carga_horaria)
