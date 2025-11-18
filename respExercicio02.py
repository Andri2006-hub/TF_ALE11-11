#respExercio02.py
class Aluno:
    def __init__(self, nome,matricula,curso):
        self.nome = nome
        self.curso = curso
        self.matricula = matricula
        self.notas = notas = []

    def adicionar_notas(self):
    self.notas.append(float(nota)
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
            return round(sum(self.notas) / len(self.notas), 2)
            def status(self):
                media = self.calcular_media()
                if media >= 7.0:
                    return "Aprovado"
                else:
                    return "Reprovado"
#Exemplo de uso conforme solicitado
if __name__ == "__main__":
aluno = Aluno("Joao Silva", "2023001", "Engenharia de Software") 
aluno.adicionar_notas(8.5)
aluno.adicionar_notas(7.0)
aluno.adicionar_notas(9.2)
print(f"Media:
{aluno.calcular_media()}")
 aluno.status()
