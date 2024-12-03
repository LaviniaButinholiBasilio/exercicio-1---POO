class Turma:
    def __init__(self, nome, professor, disciplina):
        self.nome = nome
        self.professor = professor
        self.disciplina = disciplina
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

    def excluir_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def verificar_aluno_na_turma(self, aluno):
        return aluno in self.alunos

    def obter_nomes_alunos(self):
        return [aluno.nome for aluno in self.alunos]

    def obter_nome_professor(self):
        return self.professor.nome
