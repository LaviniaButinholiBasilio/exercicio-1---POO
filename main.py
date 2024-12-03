from aluno import Aluno
from professor import Professor
from disciplina import Disciplina
from turma import Turma
from curso import Curso


aluno1 = Aluno("João")
aluno2 = Aluno("Maria")
aluno3 = Aluno("Carlos")


professor1 = Professor("Dr. Pedro")
professor2 = Professor("Dra. Ana")


disciplina1 = Disciplina("Matemática")
disciplina2 = Disciplina("Física")


turma1 = Turma("Turma A", professor1, disciplina1)
turma2 = Turma("Turma B", professor2, disciplina2)


turma1.adicionar_aluno(aluno1)
turma1.adicionar_aluno(aluno2)
turma2.adicionar_aluno(aluno3)


curso = Curso("Engenharia")


curso.adicionar_turma(turma1)
curso.adicionar_turma(turma2)


print("Alunos no curso:", curso.obter_nomes_alunos())
print("Professores no curso:", curso.obter_nomes_professores())
print("Disciplinas no curso:", curso.obter_disciplinas())


curso.excluir_aluno_do_curso(aluno2)
print("Alunos após exclusão de Maria:", curso.obter_nomes_alunos())
